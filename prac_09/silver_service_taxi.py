from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Fancy taxi with flagfall and higher price based on specialization."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # base price_per_km from Taxi class variable
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare including flagfall."""
        return round(self.flagfall + super().get_fare(), 2)

    def __str__(self):
        return (
            f"{super().__str__()}, ${self.price_per_km:.2f}/km "
            f"plus flagfall of ${self.flagfall:.2f}"
        )
