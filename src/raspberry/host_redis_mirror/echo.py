from RedisWrapper import RedisWrapper
import time


def main():
    redisWrapper = RedisWrapper()
    subscriber_obj = redisWrapper.subscriber_obj()
    subscriber_obj.subscribe('to_redis')

    print("Hearing messages from ROS2...")

    for message in subscriber_obj.listen():
        if message['type'] == 'message':
            data = message['data'].decode('utf-8')
            print("Heard: " + data)

if __name__ == '__main__':
    main()
