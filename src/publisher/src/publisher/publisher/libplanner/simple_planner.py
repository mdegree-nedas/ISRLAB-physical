import rclpy
from rclpy.node import Node

import random


TIMER = 1

class Planner(Node):
    def __init__(self, node, timer=TIMER):
        super().__init__('simple_planner')
        self.node_ = node
        self.timer_ = timer
        self.loop_ = self.create_timer(self.timer_, self.__loop_callback_)
        self.movs_ = ['right', 'left', 'forward', 'back', 'stop']

    def __loop_callback_(self):
        mov = random.choice(self.movs_)

        if mov == 'right':
            self.node_.movement.turn_right()

        elif mov == 'left':
            self.node_.movement.turn_left()

        elif mov == 'forward':
            self.node_.movement.go_forward()

        elif mov == 'back':
            self.node_.movement.go_back()

        elif mov == 'stop':
            self.node_.movement.stop()
