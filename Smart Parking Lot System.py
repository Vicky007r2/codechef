class ParkingLot:
    def __init__(self, vehicles):
        self.vehicles = vehicles
    def duplicates(self):
        dup = []
        for i in self.vehicles:
            if self.vehicles.count(i) > 1 and i not in dup:
                dup.append(i)
        return dup

    def unique_count(self):
        return len(set(self.vehicles))
vehicles = [101, 105, 110, 101, 115, 105]
p = ParkingLot(vehicles)

print("Duplicate Vehicles:", p.duplicates())
print("Unique Vehicles:", p.unique_count())
