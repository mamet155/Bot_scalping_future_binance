import time, random
from mode import MODE_NAME
from config import *
from api import *
from notifier import send

print(f"🔥 BOT START — MODE {MODE_NAME}")
send(f"🔥 BOT START — MODE {MODE_NAME}")

start_balance = get_balance()
open_pos = {}

for s in SYMBOLS:
    set_margin_type(s, "ISOLATED")
    set_leverage(s, LEVERAGE)

def calc_qty(symbol):
    price = get_price(symbol)
    notional = MARGIN_PER_TRADE * LEVERAGE
    return round(notional / price, 3)

while True:
    try:
        bal = get_balance()
        print(f"💗 BALANCE: {bal:.2f} USDT")

        for sym in SYMBOLS:
            if sym not in open_pos:
                side = random.choice(["BUY","SELL"])
                qty  = calc_qty(sym)
                market_order(sym, side, qty)

                open_pos[sym] = {"side": side, "qty": qty, "entry_bal": bal, "peak": 0}
                send(f"🚀 OPEN {sym} {side} | QTY {qty}")

            else:
                pos = open_pos[sym]
                pnl = bal - pos["entry_bal"]
                pos["peak"] = max(pos["peak"], pnl)

                if pnl <= STOP_LOSS_PCT * MARGIN_PER_TRADE:
                    close_position(sym, pos["side"], pos["qty"])
                    send(f"❌ SL {sym}")
                    del open_pos[sym]

                elif pos["peak"] > 0:
                    drop = pos["peak"] - pnl
                    if drop >= TRAILING_PROFIT_PCT * pos["peak"]:
                        close_position(sym, pos["side"], pos["qty"])
                        send(f"✅ TP {sym}")
                        del open_pos[sym]

        time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        send("🛑 BOT STOP")
        break
