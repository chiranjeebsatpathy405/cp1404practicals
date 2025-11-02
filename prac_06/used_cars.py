"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

def main():

    # New 'limo' Car object is created
    limo = Car("Limo", 100)
    print(f"Limo car created with {limo.fuel} units of fuel.")

    # Add 20 more units of fuel with add_fuel() method
    limo.add_fuel(20)
    print(f"After adding fuel, limo now has {limo.fuel} units of fuel.")

    # Drive the car for 115 km
    distance_driven = limo.drive(115)
    print(f"Limo actually drove {distance_driven} km.")

    # Now Print the car object to trigger the __str__ method
    print(limo)

if __name__ == "__main__":
    """ Estimate: 5 hours
    Actual: 3 hours """
    main()
