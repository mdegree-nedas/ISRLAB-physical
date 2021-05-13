from freenove_4WD_smart_car.core import Freenove_4wd_smart_car
from freenove_4WD_smart_car.template import *


def main():
    freen = Freenove_4wd_smart_car()
    freen.sensors.lightsensor.read(_callback=lightsensor_read_callback)
    freen.sensors.ultrasound.read(_callback=ultrasound_read_callback)
    freen.sensors.linetracker.read(_callback=linetracker_read_callback)


if __name__ == "__main__":
    main()
