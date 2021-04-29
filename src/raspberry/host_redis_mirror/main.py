import time
import yaml

from redis_wrapper import RedisWrapper


def main():
    redis_wrapper = RedisWrapper()
    subscriber_obj = redis_wrapper.subscriber_obj()
    subscriber_obj.subscribe('to_redis')

    print("Hearing messages from ROS2...")

    for message in subscriber_obj.listen():
        if message['type'] == 'message':
            data = from_yaml_to_dict(message['data'].decode('utf-8'))
            print("Heard: " + str(data))
            redis_wrapper.publish("from_redis", "I heard it (from HOST)")

def from_yaml_to_dict(yaml_str):
    return yaml.load(yaml_str)

if __name__ == '__main__':
    main()
