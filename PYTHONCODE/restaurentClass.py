class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Use self.number_served instead of number_served

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type in this restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"The restaurant {self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"The number of customers: {self.number_served}")

    def increment_number_served(self, increment):
        self.number_served += increment
        print(f"Incremented number of customers served by {increment}. New total: {self.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        print(f"The ice cream flavors are {self.flavors}")

# Instances of Restaurant and IceCreamStand
my_restaurant1 = Restaurant("Tamarind", 'Indian')
my_restaurant2 = Restaurant("Planet Diner", 'American')
my_restaurant3 = Restaurant("Giacomos", 'Italian')

# Method calls
my_restaurant1.describe_restaurant()
my_restaurant1.open_restaurant()
my_restaurant1.set_number_served(20)
my_restaurant1.increment_number_served(22)

ice_cream = IceCreamStand('B & R', 'USA', ['Vanilla', 'Butter_scotch', 'Strawberry'])

ice_cream.describe_restaurant()
ice_cream.open_restaurant()