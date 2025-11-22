class Car:
    """Represent a Car object."""

    def __init__(self, name="Car", fuel: float = 0):
        # one unit of fuel drives one kilometre
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount: float):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance: float):
        #Drive given distance if car has enough fuel or drive until fuel runs out.
        #Return the distance actually driven.
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    def __str__(self):
        # using the formatcar.py clas
        return f"{self.name}, fuel={int(self.fuel)}, odometer={int(self.odometer)}"