from guitar import Guitar


def main():

    print("My guitars!")

    guitars = []

    # --- User input loop uncomment if input is required manually

    """ name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ") """

    # --- For Testing  (uncomment while testing) ---
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # ---  results output---
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(
            f"Guitar {i}: {guitar.name:>20} ({guitar.year}), "
            f"worth ${guitar.cost:10,.2f}{vintage_string}"
        )


if __name__ == "__main__":
    main()