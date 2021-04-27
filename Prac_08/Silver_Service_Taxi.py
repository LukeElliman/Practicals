from Prac_08.taxi import Taxi

class SilverTaxi(Taxi):
    """Specialized version of taxi that includes fanciness"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initalize a SilverTaxi Class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string with Silver Taxi info"""
        return f"{self.name}, fuel={self.fuel}, {self.current_fare_distance}km on current fare," \
               f"${self.price_per_km}/km plus flagfall of {self.flagfall}"

    def get_fare(self):
        """Get price for current fare"""
        return self.flagfall + super().get_fare()



