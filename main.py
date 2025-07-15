from trading.strategy import run_strategy
import time
import os

print("🤖 ZirveTahmin Bot başlatıldı. Mod:", os.getenv("MODE"))
while True:
    try:
        run_strategy()
        time.sleep(10)
    except Exception as e:
        print(f"HATA: {e}")
        time.sleep(5)