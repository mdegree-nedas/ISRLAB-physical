from freenove_4WD_smart_car.core import Freenove_4wd_smart_car


def callb():
    print("callb")


def main():
    freen = Freenove_4wd_smart_car()
    freen.actuators.motion.commands.go_backward(_callback=callb)


if __name__ == "__main__":
    main()
