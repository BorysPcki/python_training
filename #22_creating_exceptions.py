class TooColdException(Exception):

    def __init__(self, temp):
        super().__init__("Temperature {} is below absolute zero!".format(temp))


def celsius_to_kelvin(temp):
    if temp < -273.15:
        raise TooColdException(temp)
    return temp + 273.15


try:
    print(celsius_to_kelvin(-300))
except TooColdException:
    print("Too cold!")
