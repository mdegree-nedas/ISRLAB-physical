import json
import sys
from redis_interface.redis_interface import RedisMiddleware

def go_forward(data):
    print("forward function, data:", str(data))

def go_back(data):
    print("back function, data:", str(data))

middleware = RedisMiddleware("sensors", "actuators")
middleware.register_command_callback("go_forward", go_forward)
middleware.register_command_callback("go_back", go_back)

middleware.start_listen()

print("waiting for input...")
print("press s to send sensor data example")

while True:
    com = input()
    if com == "e":
        sys.exit(0)
    elif com == "s":
        # send a sensor data
        middleware.send_sensor_data('{"sensor_name": "ultrasound", "data": [1,2,3,4,5,6]}')
    else:
        sys.exit(0)
