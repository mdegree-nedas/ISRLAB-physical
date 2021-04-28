import json

class Move:
    def __init__(self, linear_x=0.0, linear_y=0.0, linear_z=0.0, angular_x=0.0, angular_y=0.0, angular_z=0.0):
        self.linear = {'x': linear_x, 'y': linear_y, 'z': linear_z}
        self.angular = {'x': angular_x, 'y': angular_y, 'z': angular_z}

    def load_from_str(self, move_str):
        obj = json.loads(move_str)
        self.linear = obj['linear']
        self.angular = obj['angular']

    def to_json(self):
        return json.dumps(self.__dict__)

    def __str__(self):
        return self.to_json()
