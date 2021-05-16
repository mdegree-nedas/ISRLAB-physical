import redis
from types import FunctionType


class RedisWrapper:
    def __init__(self, host="0.0.0.0", port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)
        self.ps = self.r.pubsub()

    def subscribe(self, actuators_topics):
        self.ps.subscribe(**actuators_topics)
        self.ps.run_in_thread(sleep_time=0.01, daemon=True)


class RedisMiddleware:
    def __init__(self):
        self.rw = RedisWrapper()
        self.h = Handlers()
        self.actuators_topics = {"motion_topic_ros_to_noros": self.h.motion_handler}
        self.receive()

    def receive(self):
        self.rw.subscribe(self.actuators_topics)


class Handlers:
    def motion_handler(self, msg):
        data = msg["data"]
        if data["command"] == "go_forward" and data["msg_type"] == "twist":
            # template.go_forward()
            print(data)


class Freenove_4wd_smart_car:
    def __init__(self):
        self.sensors = _Sensors()
        self.actuators = _Actuators()
        self.rm = RedisMiddleware()


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

    def read(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


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
    def go_forward(self, _callback=None):
        if _callback == None:
            raise NotImplementedError("_callback is not implemented")
        if not isinstance(_callback, FunctionType):
            raise RuntimeError("_callback is not callable")
        _callback()


def main():
    f = Freenove_4wd_smart_car()
    input()


if __name__ == "__main__":
    main()
