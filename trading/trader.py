import os
import time
import hashlib
import hmac
import json
import requests

API_KEY = os.getenv("GATE_API_KEY", "")
API_SECRET = os.getenv("GATE_API_SECRET", "")
BASE_URL = "https://api.gate.io/api/v4"

def _sign(payload: str, secret: str) -> str:
    return hmac.new(secret.encode(), payload.encode(), hashlib.sha512).hexdigest()

def place_order(symbol: str, side: str, amount: float, price: float) -> str:
    if not API_KEY or not API_SECRET:
        return "❌ Gate.io API key/secret eksik"
    endpoint = "/spot/orders"
    payload = {
        "currency_pair": symbol,
        "type": "limit",
        "side": side,
        "amount": str(amount),
        "price": str(price),
        "account": "spot"
    }
    t = str(int(time.time()))
    data_str = json.dumps(payload)
    sign = _sign(data_str + t, API_SECRET)
    headers = {
        "KEY": API_KEY,
        "Timestamp": t,
        "SIGN": sign,
        "Content-Type": "application/json"
    }
    res = requests.post(BASE_URL + endpoint, headers=headers, data=data_str)
    if res.status_code == 200:
        return f"✅ {side.upper()} {symbol} {amount}@{price}"
    return f"❌ Gate.io Hata: {res.text}"