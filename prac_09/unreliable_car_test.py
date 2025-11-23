from unreliable_car import UnreliableCar
test_car = UnreliableCar("Unreliable", 100, 30)
drives = 0
attempts = 100
for _ in range(attempts):
    if test_car.drive(1) > 0:
        drives += 1
print(f"Driven {drives} times out of {attempts} attempts (should be roughly ~30%)")