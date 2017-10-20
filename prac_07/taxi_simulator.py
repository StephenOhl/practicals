from taxi import Taxi
from silver_taxi import SilverTaxi

TAXIS= [Taxi("Prius",100),SilverTaxi("Limo",100,2),SilverTaxi("Hummer",200,4)]

def get_menu_option ():
    option = input("q)uit, c)hoose taxi, d)rive\n>>>")
    while option not in ['q','c','d']:
        print ("ERROR - Invalid input")
        option = input("q)uit, c)hoose taxi, d)rive\n>>>")
    return option

def get_valid_int(prompt, low, high):
    option = int(input(prompt))
    while option < low or option > high:
        print ("ERROR - Invalid option entered")
        option = int(input(prompt))
    return option

def main():
    selection = get_menu_option()
    taxi_option = -1
    bill_to_date = 0.0
    while selection != 'q':
        if selection == 'c':
            print ("Taxis available")
            count = 0
            for taxi in TAXIS:
                print (count, ". ", taxi)
                count += 1
            taxi_option = get_valid_int("Choose taxi: ", 0, 2)

        elif selection == 'd':
            my_trip = TAXIS[taxi_option]
            print ("Your bill to date is ${:.2f}".format(bill_to_date))
            distance = get_valid_int("Drive how far? ", 1, 1000)
            my_trip.drive (distance)
            print ("Your {} trip cost ${:.2f}".format(my_trip.get_name(), my_trip.get_fare()))
            bill_to_date += my_trip.get_fare()
            print("Your bill to date is ${:.2f}".format(bill_to_date))

        else:
            print ("Thank you bye bye")
        selection = get_menu_option()

main()
