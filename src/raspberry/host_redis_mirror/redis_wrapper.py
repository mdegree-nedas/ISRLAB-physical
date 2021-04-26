import redis

SERVER_ADDR = "0.0.0.0"
SERVER_PORT = 6379
DB = 0

class RedisWrapper:
    def __init__(self, host=SERVER_ADDR, port=SERVER_PORT, db=DB):
        self.r = redis.Redis(host=SERVER_ADDR, port=SERVER_PORT, db=DB)
        self.p = self.r.pubsub()

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def subscriber_obj(self):
        return self.p

    def publish(self, channel_name, data):
        return self.r.publish(channel_name, data)

if __name__ == '__main__':
    redis_wrapper = RedisWrapper()
    redis_wrapper.set('test', 'value_test')
    print('test: ' + str(redis_wrapper.get('test')))