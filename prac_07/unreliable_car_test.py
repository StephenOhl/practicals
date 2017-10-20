from unreliable_car import UnreliableCar
import random

def main():
    my_car = UnreliableCar("Bomb", 120, 60)
    print("My bomb drove ", my_car.drive(random.randint(0, 100)), "km")
main()
