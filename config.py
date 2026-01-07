# ===== API BINANCE =====
API_KEY = "ISI_API_KEY_KAMU"
API_SECRET = "ISI_API_SECRET_KAMU"

# ===== PAIR =====
SYMBOLS = ["BTCUSDT", "ETHUSDT"]

# ===== SETUP (MODE EKSTREM) =====
LEVERAGE = 100
MARGIN_PER_TRADE = 0.5     # $0.5 per posisi

# ===== STOP LOSS =====
# SL exchange-side, pas posisi baru kebuka
STOP_LOSS_PCT = -0.20     # -20% dari harga entry

# ===== TRAILING =====
# Trailing aktif kalau profit >= 10% dari margin
# Close kalau profit turun 20% dari profit puncak
TRAILING_START_PCT = 0.10
TRAILING_DROP_PCT  = 0.20

# ===== SAFETY =====
MAX_DD_BALANCE = -0.80    # bot stop kalau balance turun 80%
PROFIT_ALERT_PCT = 0.50  # notif kalau profit +50% dari balance awal

# ===== LOOP =====
CHECK_INTERVAL = 3       # detik

# ===== TELEGRAM =====
TELEGRAM_ON = True
BOT_TOKEN = "ISI_BOT_TOKEN"
CHAT_ID = "ISI_CHAT_ID"
