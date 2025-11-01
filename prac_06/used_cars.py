"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)
    # New  'limo' Car object called
    limo = Car(100)
    print(f"Limo created with {limo.fuel} units of fuel.")
    # Add 20 more units of fuel with add_fuel() method
    limo.add_fuel(20)
    print(f"After adding fuel, limo now has {limo.fuel} units of fuel.")
    # Print the fuel amount in the car
    print(f"Limo has now  {limo.fuel} units of fuel.")
    # drive the car 115 km
    distance_driven = limo.drive(115)


main()
