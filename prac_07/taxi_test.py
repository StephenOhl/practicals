from taxi import Taxi

def main():
    a_taxi = Taxi("Prius 1", 100)
    a_taxi.drive(40)
    print (a_taxi, " = ", a_taxi.get_fare())
    a_taxi.start_fare()
    a_taxi.drive(18)
    print(a_taxi, " = ", a_taxi.get_fare())
main()