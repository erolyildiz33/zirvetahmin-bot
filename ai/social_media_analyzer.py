import os
import random

def analyze_sentiment(token: str) -> str:
    return random.choice([
        "🟢 Twitter olumlu",
        "🔴 Reddit FUD var",
        "🟡 Hype dengeli"
    ])