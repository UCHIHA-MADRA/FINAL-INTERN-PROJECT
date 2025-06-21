# import redis
# r = redis.Redis(host="localhost", port=6379, decode_responses=True)

# def add_to_history(user: str, msg: str):
#     r.lpush(f"history:{user}", msg)

# def get_history(user: str, limit: int = 50):
#     return r.lrange(f"history:{user}", 0, limit - 1)
