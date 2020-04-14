class Car:
    _vechile_type = "car"

    def move(self):
        print("The vehicle is moving")

    def print_vehicle_type(self):
        print(self._vechile_type)


class Ford(Car):
    name = "Punto"
    gear = 6

    def moveReverse(self):
        print("Vehicle can move reverse")

    def set_vehicle_type(self, vehicle_type):
        self._vechile_type = vehicle_type

    def print_vehicle_type(self):
        print(self._vechile_type)


carObj = Car()
carObj._vechile_type = "auto"
fordObj = Ford()

carObj.print_vehicle_type()
fordObj.print_vehicle_type()
fordObj.set_vehicle_type("Utility Vehicle")
fordObj.print_vehicle_type()

