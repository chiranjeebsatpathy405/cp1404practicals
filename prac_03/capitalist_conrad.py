import random

MAX_INCREASE = 0.175   # 17.5%
MAX_DECREASE = 0.05    # 5%
MIN_PRICE = 1.0        # minimum allowed price
MAX_PRICE = 100.0      # maximum allowed price
INITIAL_PRICE = 10.0   # starting price
FILENAME = "capitalist_conrad.txt"  # output file name

price = INITIAL_PRICE
number_of_days = 0

# open file for writing
out_file = open(FILENAME, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1

    if random.randint(1, 2) == 1:
        # price increases by up to MAX_INCREASE (17.5%)
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # price decreases by up to MAX_DECREASE (5%)
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# close file
out_file.close()