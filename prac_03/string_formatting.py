name = "Trademill nordictrack"
year = 2024
cost = 1025.90



# Using str.format()
print("I recently bought the fitness model: {}, in {}, that costed me {}".format(name, year,cost))
print("I recently bought the fitness model: {0}, in {1}, that costed me {2}".format(name, year,cost))


# using f-string formatting
print(f"I recently bought the fitness model {name} in {year}, that costed me {cost}")

# Formatting currency  3 decimal places:
print("I recently bought the fitness model {} would cost ${:,.3f}".format(name, cost))
print(f"I recently bought the fitness model {name} would cost ${cost:,.3f}")

# This loop uses enumerate, which is useful when you want both the index and value
numbers = [1, 19, 123, 456, -25]

for i, number in enumerate(numbers, 1):
    print(f"Number {i} is {number:5}")

# TODO: Use f-string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,036!

# TODO: Using a for loop with the range function and f-string formatting,
# produce the following right-aligned output (DO NOT use a list):