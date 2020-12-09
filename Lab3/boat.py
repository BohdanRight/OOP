from .vehicle import Vehicle


class Boat(Vehicle):
    def __init__(self, gas_tank, engine, wheels):
        super().__init__(gas_tank, engine, wheels)

    def accelerate(self):
        print("Boat accelerated")
        super().accelerate()

    def turn(self, direction):
        print("Boat turn to")
        super().turn(direction)

    def brake(self):
        print("Boat start brake")
        super().brake()

    def wheels(self):
        super().get_wheels()
