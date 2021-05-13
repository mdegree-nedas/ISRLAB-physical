import threading
import json
from redis_interface.redis_wrapper.redis_wrapper import RedisWrapper


class RedisMiddleware:
    def __init__(self, sensors_topic, actuators_topic):
        """
        Must pass sensors and actuators topic names
        """
        self.__validate_init_parameters(sensors_topic, actuators_topic)
        self.__redis = RedisWrapper()
        self.__sensors_topic = sensors_topic
        self.__actuators_topic = actuators_topic
        self.__listener = threading.Thread(target=self.__listen_on_actuators_topic)
        self.__command_map= dict()


    def register_command_callback(self, command_name, command_callback):
        """
        Register a callback (it will be called when listened a message with message.command_name = command_name)
        """
        self.__command_map[command_name] = command_callback

    def start_listen(self):
        """
        Start listener for messages
        """
        self.__listener.start()

    def send_sensor_data(self, sensor_data):
        """
        send sensor data
        """
        self.__validate_json(sensor_data)
        self.__publish_on_sensors_topic(sensor_data)


    def __listen_on_actuators_topic(self):
        subscr = self.__redis.subscriber_obj()
        subscr.subscribe(self.__actuators_topic)

        for message in subscr.listen():
            if message["type"] == "message":
                data = json.loads(message["data"])
                # call registered callback
                self.__command_map[data["command_name"]](data)
   
    def __publish_on_sensors_topic(self, data):
        self.__redis.publish(self.__sensors_topic, json.dumps(data))

    def __validate_json(self, obj):
        try:
            json.loads(obj)
        except:
            raise RuntimeError("Must be a JSON string")

    def __validate_init_parameters(self, sensors_topic, actuators_topic):
        if sensors_topic == None or (not isinstance(sensors_topic, str)):
            raise RuntimeError("sensors_topic must be a string")

        if actuators_topic == None or (not isinstance(actuators_topic, str)):
            raise RuntimeError("actuators_topic must be a string")

