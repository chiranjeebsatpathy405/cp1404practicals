"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When user input something which is not a number like one, two etc..
2. When will a ZeroDivisionError occur? When Denominator is Zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Can not divide by zero. Exiting...")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")