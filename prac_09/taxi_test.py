
from taxi import Taxi
# Create the taxi
my_taxi = Taxi("Prius 1", 100)
# Drive 40 km
my_taxi.drive(40)
print(my_taxi)
print("Current fare:", my_taxi.get_fare())
# Restart meter
my_taxi.start_fare()
# Drive 100 km
my_taxi.drive(100)
print(my_taxi)
print("Current fare:", my_taxi.get_fare())