import time, hmac, hashlib, requests
from config import API_KEY, API_SECRET
from mode import BASE_URL

def _sign(params):
    query = "&".join([f"{k}={v}" for k,v in params.items()])
    sig = hmac.new(API_SECRET.encode(), query.encode(), hashlib.sha256).hexdigest()
    return query + "&signature=" + sig

def _headers():
    return {"X-MBX-APIKEY": API_KEY}

def get_balance():
    url = BASE_URL + "/fapi/v2/balance"
    p = {"timestamp": int(time.time()*1000)}
    r = requests.get(url+"?"+_sign(p), headers=_headers()).json()
    for i in r:
        if i["asset"] == "USDT":
            return float(i["balance"])
    return 0.0

def get_price(symbol):
    url = BASE_URL + "/fapi/v1/ticker/price"
    r = requests.get(url, params={"symbol":symbol}).json()
    return float(r["price"])

def set_leverage(symbol, lev):
    url = BASE_URL + "/fapi/v1/leverage"
    p = {"symbol":symbol, "leverage":lev, "timestamp":int(time.time()*1000)}
    requests.post(url+"?"+_sign(p), headers=_headers())

def set_margin_type(symbol, mtype="ISOLATED"):
    url = BASE_URL + "/fapi/v1/marginType"
    p = {"symbol":symbol, "marginType":mtype, "timestamp":int(time.time()*1000)}
    requests.post(url+"?"+_sign(p), headers=_headers())

def market_order(symbol, side, qty):
    url = BASE_URL + "/fapi/v1/order"
    p = {
        "symbol":symbol,
        "side":side,
        "type":"MARKET",
        "quantity":qty,
        "timestamp":int(time.time()*1000)
    }
    return requests.post(url+"?"+_sign(p), headers=_headers()).json()

def close_position(symbol, side, qty):
    opp = "SELL" if side=="BUY" else "BUY"
    return market_order(symbol, opp, qty)
