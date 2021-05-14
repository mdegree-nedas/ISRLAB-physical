from geometry_msgs.msg import Twist
import time

def main():
    i = 0
    rcp = RCP()
    while True:
        time.sleep(1)
        msg = Twist()
        msg.linear.x = 0.0
        msg.linear.y = 1.0
        msg.linear.z = 2.0
        msg.angular.x = 0.0
        msg.angular.y = 1.0
        msg.angular.z = 2.0
        i = i + 1
        rcp.rm.send("topic", "command", msg)
        print("{} : {}".format(i, str(msg)))


## INTERFACE
class _TwistMsg:
    def __init__(self, topic, command, msg):
        self.topic = topic
        self.command = command
        self.data = {}
        self.data["linear"] = {}
        self.data["angular"] = {}
        self.data["linear"]["x"] = msg.linear.x
        self.data["linear"]["y"] = msg.linear.y
        self.data["linear"]["z"] = msg.linear.z
        self.data["angular"]["x"] = msg.angular.x
        self.data["angular"]["y"] = msg.angular.y
        self.data["angular"]["z"] = msg.angular.z


## BROKER
import json
import redis

class _Converter:
    def to_json(self, obj):
        return json.dumps(obj.__dict__)

class _RedisWrapper:
    def __init__(self, host="0.0.0.0", port=6379, db=0):
        self.r = redis.Redis(host, port, db)

    def publish(self, topic, msg):
        self.r.publish(topic, msg)

class _RedisMiddleware:
    def __init__(self):
        self.rw = _RedisWrapper()
        self.cv = _Converter()

    def send(self, topic, command, msg):
        msg = _TwistMsg(topic, command, msg)
        msg_json = self.cv.to_json(msg)
        self.rw.publish(topic, msg_json)


## CORE
class RCP:
    def __init__(self):
        self.rm = _RedisMiddleware()
