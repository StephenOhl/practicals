"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car
from prac_08.car import Car

def main():
    """Demo test code to show how to use car class."""

    my_car = Car("mazda",80)
    my_car.drive(30)
    limo = Car("ford", 100)
    limo.add_fuel(20)
    print("fuel = ", limo.fuel)
    limo.drive(115)
    print("odometer reading = ", limo.odometer)
    print(limo)
    print ("make = {}, fuel = {}, odometer reading = {}".format(limo.name, limo.fuel, limo.odometer))
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))


main()
