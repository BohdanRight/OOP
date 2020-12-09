from .vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, gas_tank, engine, wheels):
        super().__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print("Car accelerated")
        super().accelerate()

    def turn(self, direction):
        print("Car turn to")
        super().turn(direction)

    def brake(self):
        print("Car break")
        super().brake()

    def wheels(self):
        super().get_wheels()

