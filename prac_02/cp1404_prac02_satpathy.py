# Python Functions Code


import random  # to generate random numbers
import math    # For mathematical functions

# 5. Name functions using meaningful verb phrases
def find_hypotenuse(side_a, side_b, required_precision=3): # 2. Pass parameters by position and use default value
    """
    Calculate the hypotenuse of a right triangle.
    Returns:- float or None: The calculated and rounded hypotenuse or None if inputs are invalid.
    """
    # 4. Single Responsibility Principle(SRP): Calculation and validation.
    if side_a <= 0 or side_b <= 0:
        return None  # 3. invalid input

    hypotenuse = math.sqrt(side_a**2 + side_b**2)
    return round(hypotenuse, required_precision) # 3. Return a single value

def find_area(side_a, side_b):
    """Calculates the area of the right triangle (0.5 * a * b)."""
    if side_a <= 0 or side_b <= 0:
        return None
    return 0.5 * side_a * side_b

# New Function: Takes a random number and generates area
def generate_random_area(min_side=1, max_side=10):
    """
    Generates two random integers for the sides, calculates their area, and
    returns both the sides and the area.
    """
    # Use random.randint to select side lengths
    a = random.randint(min_side, max_side)
    b = random.randint(min_side, max_side)

    # Reusing area calculation function
    area = find_area(a, b)

    # 3. Return multiple values
    return a, b, area

def calculate_angle_degrees(opposite_side, adjacent_side):
    """
    Calculates the internal angle in degrees.
    """
    if adjacent_side == 0:
        return 90.0

    angle_radians = math.atan(opposite_side / adjacent_side)
    angle_degrees = math.degrees(angle_radians)
    return round(angle_degrees, 2)

# 4. SRP: handles display only
def show_triangle_summary(a, b, hypotenuse, angle_a):
    """show the result"""
    if hypotenuse is None:
        print(f"Error: Invalid dimensions  (A={a}, B={b}). Sides should be positive.")
    else:
        print(f"Triangle (A={a}, B={b}): Hypotenuse={hypotenuse}, Angle A={angle_a}°")

# 6. Test functions
def execute_tests():
    """
    Tests the functions.
    """
    print("\n--- Running Tests (6) ---")

    # Test 1: Pythagorean Triple (3, 4, 5)
    a1, b1 = 3, 4
    hyp1 = find_hypotenuse(a1, b1)
    print(f"Test 1: Hypotenuse({a1}, {b1}) -> {hyp1} (Expected: 5.0)")

    # Test 2: Use math.ceil() on a random float
    random_float_side = random.uniform(1.1, 5.9) # Value between 1.1 and 5.9
    a2 = math.ceil(random_float_side)
    b2 = 7.0
    hyp2 = find_hypotenuse(a2, b2)
    print(f"Test 2 (ceil): A=ceil({random_float_side:.2f})={a2}, B={b2} -> Hyp: {hyp2}")

    # Test 3: Use math.floor() on a random float
    a3 = 8.0
    b3 = math.floor(random_float_side)
    hyp3 = find_hypotenuse(a3, b3)
    print(f"Test 3 (floor): A={a3}, B=floor({random_float_side:.2f})={b3} -> Hyp: {hyp3}")

    # Test 4: Demonstrating the random area function
    rand_a, rand_b, rand_area = generate_random_area(min_side=5, max_side=15)
    print(f"\nTest 4 (Random Area): sides A={rand_a}, B={rand_b}. Area: {rand_area}")

    # Test 5: Invalid input, should return None
    a5, b5 = 0, 5
    hyp5 = find_hypotenuse(a5, b5)
    print(f"Test 5: Hypotenuse({a5}, {b5}) -> {hyp5} (Expected: None)")

    # Test 6: Returning and unpacking multiple values
    a6, b6 = 5, 12
    # 3. Unpacking multiple values
    side_a, side_b, hyp, area, angle_a = a6, b6, find_hypotenuse(a6, b6), find_area(a6, b6), calculate_angle_degrees(a6, b6)
    print(f"Test 6: Properties(5, 12) -> Hyp: {hyp}, Area: {area}, Angle A: {angle_a}°")

    print("--- Tests Complete ---")

# Main program execution block (1. Implement Python programs using functions)
if __name__ == "__main__":

    print("--- Right Triangle Program (1) ---")

    # Ex 1: Passing parameters by position
    user_a = 6.0
    user_b = 8.0

    hypotenuse = find_hypotenuse(user_a, user_b)
    angle_a = calculate_angle_degrees(user_a, user_b)

    # Calling the summary function (4. SRP)
    show_triangle_summary(user_a, user_b, hypotenuse, angle_a)

    # Ex 1: Demonstrating keyword arguments
    user_a_2 = 1.5
    user_b_2 = 2.5
    # 2. Passing by keyword
    hypotenuse_precise = find_hypotenuse(side_a=user_a_2, side_b=user_b_2)

    print(f"\nEx 1: Hypotenuse({user_a_2}, {user_b_2}): {hypotenuse_precise}")

    # Ex 2: Running the random area generator
    rand_a, rand_b, rand_area = generate_random_area()
    print(f"\nEx 2: Randomly generated area (A={rand_a}, B={rand_b}): {rand_area}")

    # 6. Call the function that systematically tests the others
    execute_tests()