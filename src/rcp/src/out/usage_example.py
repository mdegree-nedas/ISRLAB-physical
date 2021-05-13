from freenove_4WD_smart_car.core import Freenove_4wd_smart_car
import freenove_4WD_smart_car.template as template


def main():
    freen = Freenove_4wd_smart_car()
    freen.sensors.ultrasound.read(_callback=template.ultrasound_read_callback)
    freen.actuators.motion.commands.go_forward(
        _callback=template.motion_go_forward_callback
    )


if __name__ == "__main__":
    main()
