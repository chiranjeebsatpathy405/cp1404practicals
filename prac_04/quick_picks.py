import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate user-specified number of quick pick lottery lines."""
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        # Print each number in 2-character width, right-aligned
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate one quick pick of unique random numbers sorted in ascending order."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()