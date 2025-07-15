import random
import os

def is_token_safe(symbol: str) -> bool:
    if random.random() < 0.2:
        return False
    return True