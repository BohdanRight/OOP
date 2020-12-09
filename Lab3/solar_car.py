from .car import Car


class SolarCar(Car):

    def __init__(self, gas_tank, engine, wheels):
        super().__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print("Solar ")
        super().accelerate()

    def turn(self, direction):
        print("Solar")
        super().turn(direction)

    def brake(self):
        print("Solar")
        super().brake()

    def wheels(self):
        super().get_wheels()
