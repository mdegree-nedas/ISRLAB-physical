import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from virt_redis_mirror.RedisWrapper import RedisWrapper


ROS2_TOPIC = 'from_ros2'
REDIS_TOPIC = 'to_redis'


class Translater(Node):
    def __init__(self):
        super().__init__("translater")
        self.redis = RedisWrapper()
        self.sub = self.create_subscription(String, ROS2_TOPIC, self.listener_callback, 10)
        self.get_logger().info("Translater online")

    def listener_callback(self, msg):
        self.get_logger().info("Forward message '{}' from ros2 topic '{}' to redis topic '{}'".format(msg.data, ROS2_TOPIC, REDIS_TOPIC))
        self.redis.publish(REDIS_TOPIC, msg.data)
        

def main(args=None):
    rclpy.init(args=args)

    translater = Translater()

    rclpy.spin(translater)

    translater.destroy_node()
    rclpy.shutdown()
