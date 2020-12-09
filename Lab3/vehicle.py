from .engine import Engine
from .gas_tank import GasTank
from .wheels import Wheels
from .driveable import Driveable


class Vehicle(Driveable):
    def __init__(self, gas_tank: GasTank, engine: Engine, wheels: Wheels = 0):
        self.gas_tank = gas_tank
        self.engine = engine
        self.wheels = wheels
        self.speed = 0

    def get_wheels(self):
        if self.wheels.get_count() == 0:
            print("Not wheels")
        else:
            print('Wheels count: ' + str(self.wheels.get_count()))

    def accelerate(self):
        self.speed = self.speed + self.engine.get_power()
        print("Speed: ", self.speed, " km/h")

    def turn(self, direction):
        print(str(direction))

    def brake(self):
        while self.speed != 0:
            self.speed = self.speed - (self.speed / 2)
            if self.speed == 1:
                self.speed = 0
                break
            print("Speed: ", self.speed, " km/h")
            break
        print("Stop")
