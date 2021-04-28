import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from geometry_msgs.msg import Twist
from rosidl_runtime_py import message_to_ordereddict
import json

from virt_redis_mirror.redis_wrapper import RedisWrapper
import threading


FROM_ROS2_TOPIC = 'cmd_vel'
TO_ROS2_TOPIC = 'to_ros2'
TO_REDIS_TOPIC = 'to_redis'
FROM_REDIS_TOPIC = 'from_redis'


class Translater(Node):
    def __init__(self):
        super().__init__("translater")
        self.redis = RedisWrapper()
        # ROS2 topic -> REDIS topic
        self.sub = self.create_subscription(Twist, FROM_ROS2_TOPIC, self.ros2_listener_callback, 10)
        # REDIS topic -> ROS2 topic
        self.pub = self.create_publisher(String, TO_ROS2_TOPIC, 10)
        self.redis_listener = threading.Thread(target=self.redis_topic_listener)
        self.get_logger().info("Translater online")

    # ROS2 topic -> REDIS topic
    def ros2_listener_callback(self, msg):
        data = self.__from_twist_to_json(msg)
        self.get_logger().info("Forward message '{}' from ros2 topic '{}' to redis topic '{}'".format(data, FROM_ROS2_TOPIC, TO_REDIS_TOPIC))
        self.redis.publish(TO_REDIS_TOPIC, data)

    # REDIS topic -> ROS2 topic
    def redis_topic_listener(self):
        subscriber_obj = self.redis.subscriber_obj()
        subscriber_obj.subscribe(FROM_REDIS_TOPIC)

        for message in subscriber_obj.listen():
            if message['type'] == 'message':
                data = message['data'].decode('utf-8')
                self.get_logger().info("Forward message '{}' from redis topic '{}' to ros2 topic '{}'".format(data, FROM_REDIS_TOPIC, TO_ROS2_TOPIC))
                msg = String()
                msg.data = "Heard: {}".format(data)
                self.pub.publish(msg)

    def start_redis_listener(self):
        self.redis_listener.start()

    def __from_twist_to_json(self, twist_msg):
        return json.dumps(message_to_ordereddict(twist_msg))


def main(args=None):
    rclpy.init(args=args)

    translater = Translater()
    
    translater.start_redis_listener()
    rclpy.spin(translater)

    translater.destroy_node()
    rclpy.shutdown()
