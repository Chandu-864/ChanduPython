class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year
        self.odometer = 0
    def description_of_car(self):
        print(f"This car is {self.company} model {self.model} which was made in year {self.year}")
    def read_odometer(self):
            print(f"This car has {self.odometer} miles in it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
         self.odometer += miles

my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.description_of_car())
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()