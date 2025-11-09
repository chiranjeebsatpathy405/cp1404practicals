"""
Read guitars from CSV into Guitar objects, display, sort (by year), prompt for new guitars,
and save back to CSV.
Estimated Time : 2 hours.
"""
from __future__ import annotations

import csv
from pathlib import Path
from typing import List

from guitar import Guitar

Guitar_DATA_FILE = "guitars.csv"

def load_guitars(path: str | Path = Guitar_DATA_FILE) -> List[Guitar]:
    """Load guitars from a CSV file with format: Name,Year,Cost."""
    guitars: List[Guitar] = []
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].startswith('#'):
                continue
            try:
                name, year, cost = row[0].strip(), int(row[1]), float(row[2])
            except (IndexError, ValueError):
                continue
            guitars.append(Guitar(name, year, cost))
    return guitars
def save_guitars(guitars: List[Guitar], path: str | Path = Guitar_DATA_FILE) -> None:
    """Save guitars to CSV with format: Name,Year,Cost."""
    with open(path, 'w', newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        for g in guitars:
            writer.writerow([g.name, g.year, f"{g.cost}"])


def display_guitars(guitars: List[Guitar]) -> None:
    for g in guitars:
        print(g)


def prompt_new_guitars() -> List[Guitar]:
    """Prompt user to enter new guitars. Blank name to finish."""
    print("Enter your new guitars (blank name to finish)")
    new: List[Guitar] = []
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        try:
            year = int(input("Year: ").strip())
            cost = float(input("Cost: $ ").strip())
        except ValueError:
            print("Invalid number; guitar not added.")
            continue
        new.append(Guitar(name, year, cost))
    return new


def main():
    path = Path(Guitar_DATA_FILE)
    if not path.exists():
        print(f"{Guitar_DATA_FILE} not found. Create it first.")
        return

    guitars = load_guitars(path)
    print("Guitars loaded:")
    display_guitars(guitars)

    guitars.sort()  # uses Guitar.__lt__ (by year)
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Add new guitars
    added = prompt_new_guitars()
    if added:
        guitars.extend(added)
        # keep file order tidy: sort before writing
        guitars.sort()
        save_guitars(guitars, path)
        print(f"Saved {len(guitars)} guitars to {path}")
    else:
        print("No new guitars added.")


if __name__ == "__main__":
    main()
