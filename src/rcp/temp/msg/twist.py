import json


class Twist:
    def __init__(self, command, linear_x, linear_y, linear_z, angular_x, angular_y, angular_z):
        self.command = command
        self.linear = {"x": linear_x, "y": linear_y, "z": linear_z}
        self.angular = {"x": angular_x, "y": angular_y, "z": angular_z}
    
    def __str__(self):
        return json.dumps(vars(self))
