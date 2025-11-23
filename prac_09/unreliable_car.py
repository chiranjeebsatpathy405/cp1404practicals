import random
from car import Car
import random
from car import Car

# derived class for an UnreliableCar that inherits from Car
class UnreliableCar(Car):
    """percentage chance that the drive method will actually drive the car reliability check ."""
    # reliability: a float between 0 and 100, that represents the percentage chance that the drive method will actually drive the car
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
    """Generate a random number between 0 and 100, and only drive the car if that number is less than the car's reliability"""
    def drive(self, distance):
        """Drive only if random number < reliability."""
        chance = random.uniform(0, 100)
        if chance < self.reliability:
            return super().drive(distance)
        else:
            return 0
