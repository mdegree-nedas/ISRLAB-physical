import redis

import redis_interface.redis_wrapper.common as Common


class RedisWrapper:
    def __init__(self, host=Common.SERVER_ADDR, port=Common.SERVER_PORT, db=Common.DB):
        self.r = redis.Redis(host=host, port=port, db=db)
        self.p = self.r.pubsub()

    def set(self, key, value):
        return self.r.set(key, value)

    def get(self, key):
        return self.r.get(key)

    def subscriber_obj(self):
        return self.p

    def publish(self, channel_name, data):
        return self.r.publish(channel_name, data)
