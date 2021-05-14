# rcp: CORE MODULE
# rcp: auto-generated ros foreign broker file
# rcp: do not edit this file

from broker import RedisMiddleware


class Freenove_4wd_smart_car:
    def __init__(self):
        self.broker = RedisMiddleware()
        self.topics = self.__Topics()
        self.commands = self.__Commands()
        self.types = self.__Types()

    class __Topics:
        def __init__(self):
            self.ultrasound = "ultrasound_topic_noros_to_ros"
            self.motion = "motion_topic_ros_to_noros"

    class __Commands:
        def __init__(self):
            self.motion = self.__MotionCommands()

        class __MotionCommands:
            def __init__(self):
                self.go_forward = "go_forward"

    class __Types:
        def __init__(self):
            self.twist = "twist"
