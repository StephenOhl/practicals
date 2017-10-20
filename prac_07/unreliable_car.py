from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability ):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive_car(self, distance):
        to_drive = random.randint(0, 100)
        if to_drive < distance:
            return super.drive(distance)
        return 0