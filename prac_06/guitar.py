from datetime import date

class Guitar:
    """Guitar class with its details."""
    def __init__(self, name: str = "", year: int = 0, cost: float = 0.0):
        """Initialize a Guitar class instance with name, year, and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return formatted string of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of the guitar in years."""
        current_year = date.today().year
        return current_year - self.year


    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50
if __name__ == "__main__":
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Fender Stratocaster", 1954, 14000.00)
    print(my_guitar)
    print(f"Age: {my_guitar.get_age()} years")
    print(f"Vintage: {my_guitar.is_vintage()}")

    print(another_guitar)
    print(f"Age: {another_guitar.get_age()} years")
    print(f"Vintage: {another_guitar.is_vintage()}")