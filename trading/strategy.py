import random
import time
from ai.gpt_engine import analyze
from ai.social_media_analyzer import analyze_sentiment
from trading.risk_manager import evaluate_exit
from trading.liquidity_guard import is_token_safe
from trading.trader import place_order
from telegram.notifier import notify
import os

coins = ["ETH_USDT", "BNB_USDT", "MATIC_USDT", "ARB_USDT", "PEPE_USDT", "DOGE_USDT", "LINK_USDT"]

def run_strategy():
    coin = random.choice(coins)
    entry_price = round(random.uniform(0.1, 1500), 4)
    peak_price = round(entry_price * random.uniform(1.1, 3.0), 4)
    sentiment = analyze_sentiment(coin)
    gpt_comment = analyze(coin)

    if not is_token_safe(coin):
        notify(f"❌ {coin} riskli, atlandı.")
        return

    notify(f"🛒 AL sinyali → {coin}\n  • Giriş: {entry_price}\n  • Hype: {sentiment}\n  • GPT: {gpt_comment}")

    mode = os.getenv("MODE", "DEMO")
    amount = 0.01

    if mode == "LIVE":
        msg = place_order(coin, "buy", amount, entry_price)
        notify(msg)
    else:
        notify(f"(Demo) Alındı: {coin} @ {entry_price}")

    exit_msg = evaluate_exit(entry_price, peak_price, coin, amount, mode)
    notify(exit_msg)