# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

class User:

    def __init__(self,first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old and identifies as {self.gender}.")

    def greet_user(self):
        print(f"\n Welcome back {self.first_name}!")

user_1 = User("John", "Doe", 25, "male")

user_2 = User("Jane", "Smith", 13, "female")

user_3 = User("Riley", "Johnson", 20, "non-binary")

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

user_3.greet_user()
user_1.greet_user()
user_2.greet_user()