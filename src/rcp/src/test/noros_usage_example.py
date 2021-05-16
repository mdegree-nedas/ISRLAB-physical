import redis
import json

# from types import FunctionType
from collections.abc import Callable


class RedisWrapper:
    def __init__(self, host="0.0.0.0", port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)
        self.ps = self.r.pubsub()

    def subscribe(self, actuators_topics):
        self.ps.subscribe(**actuators_topics)
        self.ps.run_in_thread(sleep_time=0.01, daemon=True)


class RedisMiddleware:
    def __init__(self, actuators_topics):
        self._redis_wrapper = RedisWrapper()
        self.actuators_topics = actuators_topics

    def receive(self):
        self._redis_wrapper.subscribe(self.actuators_topics)


class Template:
    def go_forward_callback(self, data):
        print("this is the default callback")
        print("give to this method an implementation")
        print("or implement another callback, and assign it using:")
        print("    f = Freenove_4wd_smart_car()")
        print("    f.actuators.motion.go_forward.callback = <your-callback>")

    def ultrasound_read(self):
        print("ultrasound_read")


class Freenove_4wd_smart_car:
    def __init__(self):
        self.sensors = _Sensors()
        self.actuators = _Actuators()

        self.actuators_topics = {
            self.actuators.motion.topic: self.actuators.motion.commands.handler
        }
        self.broker = RedisMiddleware(self.actuators_topics)


class _Sensors:
    def __init__(self):
        self.ultrasound = _Ultrasound()


class _Ultrasound:
    def __init__(self):
        self.id = "ultrasound_id"
        self.type = "vector"
        self.address = "ultrasound_address"
        self.topic = "ultrasound_topic_noros_to_ros"
        self.data = None
        self.callback = None

    # def read(self, _callback=None):
    #     if _callback == None:
    #         raise NotImplementedError("_callback is not implemented")
    #     if not isinstance(_callback, FunctionType):
    #         raise RuntimeError("_callback is not callable")
    #     _callback()


class _Actuators:
    def __init__(self):
        self.motion = _Motion()


class _Motion:
    def __init__(self):
        self.id = "motion_id"
        self.address = "motion_address"
        self.topic = "motion_topic_ros_to_noros"
        self.commands = _MotionCommands()


class _MotionCommands:
    def __init__(self):
        self.go_forward = self._GoForward()

    def handler(self, msg):
        data = json.loads(msg["data"])
        if (
            data["msg_type"] == self.go_forward.data
            and data["command"] == self.go_forward.name
        ):
            self.go_forward.run(data)

    class _GoForward:
        def __init__(self):
            self.name = "go_forward"
            self.templates = Template()
            self.callback = self.templates.go_forward_callback
            self.data = "twist"

        def run(self, data):
            if self.callback == None:
                raise NotImplementedError("_callback is not implemented")
            if not isinstance(self.callback, Callable):
                raise RuntimeError("_callback is not callable")
            self.callback(data)


def print_roba(data):
    print("callback")
    print(data)


def main():
    f = Freenove_4wd_smart_car()
    # f.actuators.motion.commands.go_forward.callback = print_roba
    f.broker.receive()
    input()


if __name__ == "__main__":
    main()
