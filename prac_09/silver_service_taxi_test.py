from silver_service_taxi import SilverServiceTaxi
taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
taxi.start_fare()
taxi.drive(18)
print(taxi)
print("Fare:", taxi.get_fare())
# Assert test
assert taxi.get_fare() == 48.78, "Fare calculation is incorrect!"
