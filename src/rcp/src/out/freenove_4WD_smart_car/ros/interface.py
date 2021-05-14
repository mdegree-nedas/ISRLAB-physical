# rcp: INTERFACE MODULE
# rcp: auto-generated noros foreign interface file
# rcp: do not edit this file


class _GeometryMsgsTwist:
    def __init__(self, topic, command, msg):
        self._topic = topic
        self._command = command
        self._data = {}
        self._data["linear"] = {}
        self._data["angular"] = {}
        self._data["linear"]["x"] = msg.linear.x
        self._data["linear"]["y"] = msg.linear.y
        self._data["linear"]["z"] = msg.linear.z
        self._data["angular"]["x"] = msg.angular.x
        self._data["angular"]["y"] = msg.angular.y
        self._data["angular"]["z"] = msg.angular.z
