"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car


class Taxi(Car):
    """Special Car that includes fare costs."""
    price_per_km = 1.23 # class variable shared by all taxis
    def __init__(self, name, fuel) :
        """Initialise Taxi class"""
        super().__init__(name, fuel)
        #self.price_per_km = price_per_km
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return f"{super().__str__()}, {self.current_fare_distance}km on current fare"

    def get_fare(self):
        """Return the fare rounded to the nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance
        # round to nearest 0.10 → multiply by 10, round, divide by 10
        return round(fare * 10) / 10

    def start_fare(self):
        """Begin a new fare."""
        #self.current_fare_distance = 0
        """Return the fare based on distance driven."""
        return round(self.price_per_km * self.current_fare_distance, 2)

    def drive(self, distance):
        #track fare distance
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
