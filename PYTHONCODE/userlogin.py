class user:
    def __init__(self, First_name, Last_name, Age, Nationality):
        self.First_name = First_name
        self.Last_name = Last_name
        self.Age = Age
        self.Nationality = Nationality
        self.login = 0
    def describe(self):
        print(f"The student first name is {self.First_name}")
        print(f"The student last name is {self.Last_name}")
        print(f"The students age is {self.Age}")
        print(f"The student Nationality is {self.Nationality}")
    def greet(self):
        print(f"Hi {self.First_name} {self.Last_name} Welcome to the college!")
    
    def login_attempt(self):
        self.login += 1
        print(f"The user has logged on: {self.login} for the first time")
        print("                     and")

    def increament_login_attempt(self, increment):
        self.login += increment
        print(f"The user has logged on: {self.login} times in total ")

    def reset_login_attempts(self):
        self.login = 0
        print(f"Your account has been reset and your number of logins are {self.login}")

user1 = user('jimmy','thalati',3, 'Indian')
user1.describe()
user1.greet()
user1.login_attempt()
user1.increament_login_attempt(12)
user1.reset_login_attempts()