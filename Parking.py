class ParkingSystem:
    def __init__(self, big, medium, small):
        # Store available slots for each car type
        self.slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType):
        # Check if there's an available slot for the given car type
        if self.slots[carType] > 0:
            self.slots[carType] -= 1  # Park the car (decrease slot count)
            return True
        else:
            return False  # No available slot


# Example usage:
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))  # True
print(parkingSystem.addCar(2))  # True
print(parkingSystem.addCar(3))  # False
print(parkingSystem.addCar(1))  # False
