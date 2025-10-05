#Do-from-scratch Exercises
 #1. save name to name.txt
name = input("Enter your name: ")
file = open("name.txt", "w")  # open in write mode
file.write(name)
file.close()

# 2. greet the user
file = open("name.txt", "r")  # open in read mode
name_from_file = file.read().strip()
file.close()
print(f"Hi {name_from_file}!")


# 3. Read first two numbers from numbers.txt and add them
# numbers.txt contents:
# 17
# 42
# 400
with open("numbers.txt", "r") as file:
    first_line = file.readline()
    second_line = file.readline()

# Convert to integers and add
num1 = int(first_line.strip())
num2 = int(second_line.strip())
print(num1 + num2)


# 4. total of all numbers
total = 0
with open("numbers.txt", "r") as file:
    for line in file:  # iterate over each line
        total += int(line.strip())
print(total)