# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
class User:

    def __init__(self,first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old and identifies as {self.gender}.")

    def greet_user(self):
        print(f"\n Welcome back {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("John", "Doe", 25, "male")
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
print(user.login_attempts)