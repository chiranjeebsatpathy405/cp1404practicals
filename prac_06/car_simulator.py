#car_simulator.py
""" Estimate: 5 hours
    Actual: 2 hours and 30 minutes"""
from car import Car


def main():
    print("Let's drive!")
    car_name = input("Enter your car name: ")
    my_car = Car(car_name, 100)  # start with 100 units of fuel
    print(my_car)

    MENU = "Menu:\nd) drive\nr) refuel\nq) quit"
    choice = ""

    while choice.lower() != "q":
        print(MENU)
        choice = input("Enter your choice: ").lower()

        if choice == "d":
            drive_car(my_car)
        elif choice == "r":
            refuel_car(my_car)
        elif choice == "q":
            break
        else:
            print("Invalid choice")

        print(f"\n{my_car}")

    print(f"\nGood bye {my_car.name}'s driver.")
def drive_car(car):

    try:
        distance = float(input("How many km do you wish to drive? "))
        while distance < 0:
            print("Distance must be >= 0")
            distance = float(input("How many km do you wish to drive? "))

        distance_driven = int(car.drive(distance))
        if distance_driven < distance:
            print(f"The car drove {distance_driven}km and ran out of fuel.")
        else:
            print(f"The car drove {distance_driven}km.")
    except ValueError:
        print("Please enter a valid number.")
def refuel_car(car):

    try:
        amount = float(input("How many units of fuel do you want to add to the car? "))
        while amount < 0:
            print("Fuel amount must be >= 0")
            amount = float(input("How many units of fuel do you want to add to the car? "))

        car.add_fuel(amount)
        print(f"Added {amount} units of fuel.")
    except ValueError:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()