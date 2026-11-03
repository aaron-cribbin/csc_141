# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

class Dog:

    def __init__(self, name, age, color, breed):

        self.name = name
        self.age = age
        self.color = color
        self.breed = breed


    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog("Bud", 3, "white", "Corgi")

print(f"I named my dog {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
print(f"And they are a {my_dog.color} {my_dog.breed}.")
my_dog.roll_over()

his_dog = Dog("Spike", 7, "gray", "Pitbull")
print(f"His dog is named {his_dog.name}.")
print(f"His dog is {his_dog.age} years old.")
print(f"And they are a {his_dog.color} {his_dog.breed}.")