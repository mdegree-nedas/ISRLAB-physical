import redis

import redis_wrapper.common as Common


class RedisWrapper:
    def __init__(self, host=Common.SERVER_ADDR, port=Common.SERVER_PORT, db=Common.DB):
        self.__r = redis.Redis(host=host, port=port, db=db)
        self.__p = self.__r.pubsub()


    def set(self, key, value):
        return self.__r.set(key, value)

    def get(self, key):
        return self.__r.get(key)

    def subscribe(self, channel_name):
        self.__p.subscribe(channel_name)

    def listen(self):
        return self.__p.listen()

    def publish(self, channel_name, data):
        return self.__r.publish(channel_name, data)
