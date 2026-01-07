
import time, signal, sys
from api import (
    get_balance, get_price, set_leverage, set_margin_type,
    market_order, close_position, place_stop_loss
)
from notifier import send
from config import (
    SYMBOLS, LEVERAGE, MARGIN_PER_TRADE,
    STOP_LOSS_PCT, TRAILING_DROP_PCT, CHECK_INTERVAL
)
from mode import MODE_NAME

positions = {}
start_balance = None
profit_alert_sent = False

# 🔹 simpan profit tertinggi (ATH) setelah trailing aktif
peak_profit = {}

# ===== TRAILING SETTING =====
TRAILING_START_PCT = 0.10   # trailing aktif jika profit >= 10% dari margin

def calc_qty(price):
    return round((MARGIN_PER_TRADE * LEVERAGE) / price, 3)

def handle_exit(sig=None, frame=None):
    send("⛔ Bot dihentikan. Closing positions...")
    for s, p in list(positions.items()):
        close_position(s, p["side"], p["qty"])
    sys.exit(0)

signal.signal(signal.SIGINT, handle_exit)
signal.signal(signal.SIGTERM, handle_exit)

print(f"🔥 BOT START — {MODE_NAME}")
send(f"🤖 Bot start — {MODE_NAME}")

for s in SYMBOLS:
    set_margin_type(s, "ISOLATED")
    set_leverage(s, LEVERAGE)

start_balance = get_balance()
send(f"💖 Balance awal: {start_balance} USDT")

def open_trade(symbol, side):
    price = get_price(symbol)
    qty = calc_qty(price)
    market_order(symbol, side, qty)
    place_stop_loss(symbol, side, price, STOP_LOSS_PCT)

    positions[symbol] = {
        "side": side, "entry": price, "qty": qty
    }

    # reset peak saat open baru
    peak_profit.pop(symbol, None)

    send(f"🚀 OPEN {symbol} {side} | QTY {qty}")

def check_position(symbol):
    if symbol not in positions:
        return

    p = positions[symbol]
    now = get_price(symbol)
    entry = p["entry"]
    side = p["side"]

    # ===== HITUNG PROFIT RELATIF =====
    pnl_ratio = (now-entry)/entry if side=="BUY" else (entry-now)/entry

    # ===== KONVERSI KE PROFIT UANG (USDT) =====
    # perkiraan: profit ≈ pnl_ratio * (margin * leverage)
    profit_usdt = pnl_ratio * (MARGIN_PER_TRADE * LEVERAGE)

    # ===== AKTIFKAN TRAILING SETELAH PROFIT >= 10% MARGIN =====
    if profit_usdt >= MARGIN_PER_TRADE * TRAILING_START_PCT:
        # inisialisasi peak kalau belum ada
        if symbol not in peak_profit:
            peak_profit[symbol] = profit_usdt

        # update profit tertinggi
        if profit_usdt > peak_profit[symbol]:
            peak_profit[symbol] = profit_usdt

    # ===== TRAILING CLOSE: TURUN 20% DARI PEAK =====
    if symbol in peak_profit and peak_profit[symbol] > 0:
        drop_ratio = (peak_profit[symbol] - profit_usdt) / peak_profit[symbol]

        if drop_ratio >= TRAILING_DROP_PCT:
            close_position(symbol, side, p["qty"])
            send(f"🔐 TRAILING CLOSE {symbol} | profit turun {int(TRAILING_DROP_PCT*100)}% dari puncak")
            positions.pop(symbol, None)
            peak_profit.pop(symbol, None)

def main_loop():
    global profit_alert_sent

    while True:
        bal = get_balance()

        # ===== KILL-SWITCH =====
        if bal <= start_balance * 0.2:
            send("🚨 ACCOUNT STOP — Loss 80%. Bot berhenti.")
            break

        # ===== PROFIT ALERT =====
        if (not profit_alert_sent) and bal >= start_balance * 1.5:
            send("🎉 PROFIT ALERT — Balance +50%!")
            profit_alert_sent = True

        for s in SYMBOLS:
            if s not in positions:
                open_trade(s, "BUY")
            else:
                check_position(s)

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main_loop()
