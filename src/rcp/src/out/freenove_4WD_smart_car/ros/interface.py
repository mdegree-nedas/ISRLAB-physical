# rcp: INTERFACE MODULE
# rcp: auto-generated ros foreign interface file
# rcp: EDIT this file and insert other ros2 msg interface wrappers


class GeometryMsgsTwist:
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
