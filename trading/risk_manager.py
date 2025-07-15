from trading.trader import place_order
import os

TP_DROP = float(os.getenv("TAKE_PROFIT_DROP_PERCENT", 50)) / 100
STOP_LOSS = float(os.getenv("STOP_LOSS_PERCENT", 15)) / 100
TRAILING = float(os.getenv("TRAILING_STOP_PERCENT", 10)) / 100

def evaluate_exit(entry, peak, symbol, amount, mode):
    sl_price = entry * (1 - STOP_LOSS)
    trailing_price = peak * (1 - TRAILING)
    tp_price = peak * (1 - TP_DROP)

    def do_sell(price, reason):
        if price < entry:
            return f"⏳ {symbol}: Satış gerçekleşmedi (fiyat düşük)"
        if mode == "LIVE":
            return f"🏁 Satış ({reason}): " + place_order(symbol, "sell", amount, price)
        else:
            return f"(Demo) Satıldı ({reason}) → {symbol} @ {price}"

    if sl_price < entry:
        return do_sell(sl_price, "Stop-Loss")
    if trailing_price > entry:
        return do_sell(trailing_price, "Trailing Stop")
    if tp_price > entry:
        return do_sell(tp_price, "Take-Profit")
    return f"⏳ {symbol}: satış tetiklenmedi (Entry: {entry}, Peak: {peak})"