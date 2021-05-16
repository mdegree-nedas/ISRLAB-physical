import random
import time

from .ros.core import Freenove_4wd_smart_car

from geometry_msgs.msg import Twist


def main():
    f = Freenove_4wd_smart_car()
    while True:
        time.sleep(1)

        msg = Twist()
        msg.linear.x = random.uniform(0, 1)
        msg.linear.y = random.uniform(0, 1)
        msg.linear.z = random.uniform(0, 1)
        msg.angular.x = random.uniform(0, 1)
        msg.angular.y = random.uniform(0, 1)
        msg.angular.z = random.uniform(0, 1)

        f.broker.send(f.topics.motion, f.commands.motion.go_forward, f.types.twist, msg)


if __name__ == "__main__":
    main()
