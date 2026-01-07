Gas. Ini README final versi rapi, ringkas, dan siap kamu upload ke repo 👇
Tinggal copy–paste ke README.md.


---

Bot_scalping_future_binance

Bot scalping otomatis untuk Binance Futures (support DEMO / TESTNET & REAL).
Cocok buat yang mau coba trading pakai bot dari nol sampai jalan.


---

✨ Fitur Utama

Auto open posisi BUY / SELL

Support Isolated Margin

Stop Loss otomatis tiap open posisi

Trailing Profit (kunci profit kalau harga balik)

Risk control

Bot stop kalau drawdown > 80%

Bot close semua posisi kalau mati


Notifikasi Telegram

Alert kalau profit tembus 50% balance awal



---

📁 Struktur File

main.py      -> logic utama bot  
api.py       -> koneksi ke Binance  
config.py    -> setting bot & API  
mode.py      -> pilih DEMO / REAL  
notifier.py  -> kirim notif ke Telegram


---

🚀 Cara Pakai (Dari Nol)

1️⃣ Install Termux + Python

pkg update
pkg install python -y
pkg install git -y

2️⃣ Clone repo

git clone https://github.com/mamet155/Bot_scalping_future_binance.git
cd Bot_scalping_future_binance

3️⃣ Install library

pip install requests


---

🔑 Setup API Binance

1. Login Binance


2. Buka API Management


3. Buat API Key


4. Aktifkan:

Futures

Enable Trading



5. Simpan:

API_KEY

API_SECRET





---

🤖 Setup Bot Telegram (Notif)

1. Buka Telegram → cari @BotFather


2. /start → /newbot


3. Copy TOKEN BOT


4. Cari @userinfobot → ambil CHAT_ID




---

⚙️ Edit config.py

Buka file:

nano config.py

Isi bagian ini:

# ===== API BINANCE =====
API_KEY = "ISI_API_KEY_KAMU"
API_SECRET = "ISI_API_SECRET_KAMU"

# ===== TELEGRAM =====
TG_TOKEN = "ISI_TOKEN_BOT_TELE"
TG_CHAT_ID = "ISI_CHAT_ID_KAMU"

# ===== MODE =====
# DEMO = testnet, REAL = akun asli
MODE = "DEMO"

# ===== BOT SETTING =====
SYMBOLS = ["BTCUSDT", "ETHUSDT"]

LEVERAGE = 10
MARGIN_PER_TRADE = 0.5   # USD per posisi

STOP_LOSS_PCT = -0.20        # -20% dari margin
TRAILING_PROFIT_PCT = 0.20  # trailing 20% dari profit puncak

MAX_DD_BALANCE = -0.80      # stop bot kalau balance turun 80%
PROFIT_ALERT_PCT = 0.50     # notif kalau profit +50%

CHECK_INTERVAL = 3          # detik

Simpan:

CTRL + O → Enter → CTRL + X


---

▶️ Jalankan Bot

python main.py

Kalau sukses, bakal muncul:

BOT START - MODE DEMO
BALANCE: xxxx USDT


---

🛑 Cara Stop & Hapus Bot Lama

Stop bot

Tekan:

CTRL + C

Hapus bot lama

cd ~
rm -rf Bot_scalping_future_binance


---

⚠️ Catatan Penting

WAJIB test di DEMO dulu

Jangan langsung pakai real kalau belum paham

Bot ini scalping agresif, risiko tinggi

Semua keputusan trading tanggung jawab user



---

🧠 Ringkasannya

Bot ini dibuat buat:

Latihan trading automation

Testing strategi scalping

Belajar risk management pakai bot


Bukan buat jamin cuan, tapi alat bantu biar trading lebih disiplin.


---
