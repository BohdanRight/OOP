from Lab3.boat import Boat
from Lab3.car import Car
from Lab3.solar_car import SolarCar
from Lab3.engine import Engine
from Lab3.gas_tank import GasTank
from Lab3.wheels import Wheels


def drive_vehicle(driveable):
    driveable.get_wheels()
    driveable.accelerate()
    driveable.turn("Left")
    driveable.turn("Right")
    driveable.brake()


class Main:

    def __init__(self):
        boat = Boat(GasTank(50), Engine(100), Wheels(0))
        car = Car(GasTank(100), Engine(250), Wheels(6))
        solar_car = SolarCar(GasTank(20), Engine(500), Wheels(4))
        vehicles = [boat, car, solar_car]
        for vehicle in vehicles:
            drive_vehicle(vehicle)


Main()
