import random

#Random Function
print(random.randint(5, 20))  # line 1
#Smallest number: 5
#Largest number: 20


print(random.randrange(3, 10, 2))  # line 2
#Smallest number: 3
#Largest number: 9

print(random.uniform(2.5, 5.5))  # line 3
#Smallest possible number: 2.5
#Largest possible number: 5.5

#random number between 1 and 100 inclusive
num_between1_100 = random.randint(1, 100)
print(num_between1_100)