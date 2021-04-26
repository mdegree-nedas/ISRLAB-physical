import time

from redis_wrapper import RedisWrapper


def main():
    redis_wrapper = RedisWrapper()
    subscriber_obj = redis_wrapper.subscriber_obj()
    subscriber_obj.subscribe('to_redis')

    print("Hearing messages from ROS2...")

    for message in subscriber_obj.listen():
        if message['type'] == 'message':
            data = message['data'].decode('utf-8')
            print("Heard: " + data)
            redis_wrapper.publish("from_redis", "I heard it (from HOST)")

if __name__ == '__main__':
    main()
