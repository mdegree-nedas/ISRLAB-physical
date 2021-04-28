import time
import json

from redis_wrapper import RedisWrapper


def main():
    redis_wrapper = RedisWrapper()
    subscriber_obj = redis_wrapper.subscriber_obj()
    subscriber_obj.subscribe('to_redis')

    print("Hearing messages from ROS2...")

    for message in subscriber_obj.listen():
        if message['type'] == 'message':
            data = from_json_to_dict(message['data'].decode('utf-8'))
            print("Heard: " + str(data))
            redis_wrapper.publish("from_redis", "I heard it (from HOST)")

def from_json_to_dict(dict_str):
    return json.loads(dict_str)

if __name__ == '__main__':
    main()
