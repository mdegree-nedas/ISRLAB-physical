from redis_wrapper.redis_wrapper import RedisWrapper
import threading

def listener():
    for msg in redis.listen():
        print(msg)

redis = RedisWrapper()

redis.set("test", "value")
print("redis get: ", redis.get("test"))

redis.subscribe("sub_chan_1")
redis.subscribe("sub_chan_2")

threading.Thread(target=listener).start()

print("awaiting commands (s to send a test publish)")
while True:
    com = input()
    if com == "s":
        redis.publish("pub_chan", "Hi")
