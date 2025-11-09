from datetime import date
# Copied from Prac_06
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

    #Function to sort the list by year (oldest to newest) and display them in sorted order
    def __lt__(self, other: "Guitar") -> bool:
        """Order guitars by year (older first)."""
        if not isinstance(other, Guitar):
            return NotImplemented
        return self.year < other.year
