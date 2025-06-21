import os
import redis

def test_redis():
    # Read Redis config from environment variables
    redis_host = os.getenv('REDIS_HOST', 'localhost')
    redis_port = int(os.getenv('REDIS_PORT', 6379))
    redis_password = os.getenv('REDIS_PASSWORD', None)

    # Connect to Redis
    r = redis.Redis(host=redis_host, port=redis_port, password=redis_password)

    try:
        # Test set/get
        r.set('test_key', 'test_value')
        value = r.get('test_key')

        if value == b'test_value':
            print("Redis working")
        else:
            print("Redis test failed: unexpected value")
    except Exception as e:
        print(f"Redis test failed: {e}")

if __name__ == "__main__":
    test_redis()
