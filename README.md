

---

Bot_scalping_future_binance

Bot scalping otomatis untuk Binance Futures (support DEMO/TESTNET & REAL).
Fokus: risk control + trailing pintar biar profit gak balik nol.


---

✨ Fitur Utama

Auto open posisi BUY / SELL

Isolated margin

Stop Loss otomatis (exchange-side) saat posisi dibuka

Trailing profit pintar

Trailing baru aktif jika profit ≥ 10% dari margin

Posisi close jika profit turun 20% dari puncak


Safety

Bot stop kalau balance turun 80% (MAX_DD_BALANCE)

Profit alert kalau balance naik +50%


Notifikasi Telegram (open, close, alert)



---

📁 Struktur File

main.py      -> logic utama bot  
api.py       -> koneksi ke Binance  
config.py    -> setting bot & API  
mode.py      -> pilih DEMO / REAL  
notifier.py  -> kirim notif Telegram


---

🚀 Cara Pakai (Dari Nol)

1️⃣ Install di Termux

pkg update
pkg install python git -y

2️⃣ Clone repo

git clone https://github.com/mamet155/Bot_scalping_future_binance.git
cd Bot_scalping_future_binance

3️⃣ Install dependency

pip install requests


---

🔑 Setup API Binance

1. Login Binance → API Management


2. Buat API Key


3. Aktifkan:

Futures

Enable Trading



4. Simpan:

API_KEY

API_SECRET





---

🤖 Setup Bot Telegram (Notif)

1. Buka Telegram → cari @BotFather


2. /start → /newbot → copy TOKEN


3. Cari @userinfobot → ambil CHAT_ID




---

⚙️ Edit config.py

Buka:

nano config.py

Isi contoh (sesuaikan punyamu):

# ===== API BINANCE =====
API_KEY = "ISI_API_KEY_KAMU"
API_SECRET = "ISI_API_SECRET_KAMU"

# ===== PAIR =====
SYMBOLS = ["BTCUSDT", "ETHUSDT"]

# ===== SETUP =====
LEVERAGE = 100
MARGIN_PER_TRADE = 0.5

# ===== STOP LOSS =====
STOP_LOSS_PCT = -0.20

# ===== TRAILING =====
TRAILING_START_PCT = 0.10   # trailing aktif jika profit >= 10% margin
TRAILING_DROP_PCT  = 0.20   # close jika profit turun 20% dari puncak

# ===== SAFETY =====
MAX_DD_BALANCE = -0.80      # bot stop kalau balance -80%
PROFIT_ALERT_PCT = 0.50    # alert kalau profit +50%

# ===== LOOP =====
CHECK_INTERVAL = 3

# ===== TELEGRAM =====
TELEGRAM_ON = True
BOT_TOKEN = "ISI_BOT_TOKEN"
CHAT_ID = "ISI_CHAT_ID"

Simpan:

CTRL + O → Enter → CTRL + X


---

▶️ Jalankan Bot

python main.py


---

🛑 Stop & Bersih-bersih

Stop bot: CTRL + C

Hapus folder bot:


cd ~
rm -rf Bot_scalping_future_binance


---

⚠️ Catatan Penting

Test di DEMO dulu sebelum ke REAL.

Bot ini agresif → risiko tinggi.

Semua keputusan trading tetap tanggung jawab user.



---
