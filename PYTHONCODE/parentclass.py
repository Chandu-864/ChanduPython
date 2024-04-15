class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"The car is {self.company} {self.model} made in year {self.year}")

class Battery:
    def __init__(self, battery_size):
        self.battery_size = battery_size
        self.battery_cost = 4000

    def battery_details(self):
        print(f"The battery size is {self.battery_size} KWh and its cost is {self.battery_cost} $")

    def range(self):
        if self.battery_size <= 40:
            range_mph = 120
        elif self.battery_size > 40:
            range_mph = 220 
        print(f"The range of this battery is {range_mph} MPH")

class ElectricCar(Car):
    def __init__(self, company, model, year, battery_size):
        super().__init__(company, model, year)
        self.battery = Battery(battery_size)

my_car = ElectricCar('Honda', 'Amaze', 2023, battery_size=40)

my_car.describe_car()
my_car.battery.battery_details()
my_car.battery.range()