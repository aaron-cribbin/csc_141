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

class Admin(User):

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(["can add post", "can delete post", "can ban user"])

    def show_privileges(self):
        self.privileges.show_privileges()

class Privileges:

    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(f"\nAdmin has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

admin_user = Admin("John", "Doe", 30, "male")
admin_user.show_privileges()