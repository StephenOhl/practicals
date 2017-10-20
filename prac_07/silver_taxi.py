from taxi import Taxi

class SilverTaxi(Taxi):
    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km = Taxi.price_per_km * fanciness
        self.flag_fall = 4.50

    def drive(self, distance):
        return super().drive(distance)

    def get_fare(self):
        return round((super().get_fare() + self.flag_fall), 1)

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flag_fall)
    def give_name(self):
        return "{}".format(super.get_name())