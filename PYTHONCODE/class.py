class Restaurent:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurent_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurent(self):
        print(f"The restaurent name is {self.restaurent_name}")
        print(f"The cuisine type in this restaurent is {self.cuisine_type}")
    def open_restaurent(self):
        print(f"The restaurent {self.restaurent_name} is open")
My_restaurent1 = Restaurent("Tamarind", 'indian')
My_restaurent2 = Restaurent("Planet diner", 'American')
My_restaurent3 = Restaurent("Giacomos", 'Italian')
print("_____________________________________________________________")
My_restaurent1.describe_restaurent()
My_restaurent1.open_restaurent()
print("")
My_restaurent2.describe_restaurent()
My_restaurent2.open_restaurent()
print("")
My_restaurent3.describe_restaurent()
My_restaurent3.open_restaurent()
print("_____________________________________________________________")