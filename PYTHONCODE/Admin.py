class user:
    def __init__(self, First_name, Last_name, Age, Nationality):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Nationality = Nationality
        
    def describe(self):
        print(f"The student first name is {self.First_name}")
        print(f"The student last name is {self.Last_name}")
        print(f"The students age is {self.Age}")
        print(f"The student Nationality is {self.Nationality}")
    def greet(self):
        print(f"Hi {self.First_name} {self.Last_name} Welcome to the college!")

class Admin(user):
    def __init__(self, First_name, Last_name, Age, Nationality, priviliges):
        super().__init__(First_name, Last_name, Age, Nationality)
        self.priviliges = priviliges

    def show_priviliges(self):
        self.priviliges = ["can add post", "can delete post", "can ban user"]
        print(f"The {self.First_name} {self.Last_name} is a Administrator")
        print(f"The admin {self.First_name} {self.Last_name} has special previliges like {self.priviliges} and so on")

user1 = user('jimmy','thalati',3, 'Indian')
user2 = user('sam','lab',5, 'Indian')
user3 = user('chandu','thalati',23, 'Indian')
user4 = user('seeenu','thalati',54, 'Indian')

user1.describe()
user1.greet()
print("")
user2.describe()
user2.greet()
print("")
user3.describe()
user3.greet()
print("")
user4.describe()
user4.greet()
print("")

admin1 = Admin('Padma', 'Mummadi', 56, 'Indian', 'priviliges')
admin1.describe()
admin1.greet()
admin1.show_priviliges()