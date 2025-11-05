import redis
from typing import List, Tuple

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_top_products(user_id: int) -> List[Tuple[str, int]]:
    results = r.zrevrange(f"user:{user_id}:scores", 0, 4, withscores=True)

    cleaned = []
    for product_key, score in results:
        # ✅ Extract real product ID: p1
        product_id = product_key.split(":")[1] if ":" in product_key else product_key
        cleaned.append((product_id, int(score)))
    
    print(f"✅ Redis cleaned IDs: {cleaned}")
    return cleaned
