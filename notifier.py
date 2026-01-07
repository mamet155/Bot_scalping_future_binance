import requests
from config import TG_TOKEN, TG_CHAT_ID

def send(msg):
    try:
        url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
        data = {"chat_id": TG_CHAT_ID, "text": msg}
        requests.post(url, data=data, timeout=5)
    except:
        pass
