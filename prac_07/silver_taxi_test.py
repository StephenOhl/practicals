from silver_taxi import SilverTaxi

def main():
    my_taxi = SilverTaxi ("Hummer", 200, 2)
    my_taxi.drive(18)
    print(my_taxi, " = ${:.2f}".format(my_taxi.get_fare()), "(yikes)")
    print (my_taxi)
main()