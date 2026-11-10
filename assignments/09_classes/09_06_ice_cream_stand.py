# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} serves {self.flavors} ice cream.")

ice_cream_stand = IceCreamStand("The Parlor", "Ice Cream", ["vanilla", "chocolate", "sherbet", "mint chocolate chip"])

ice_cream_stand.describe_restaurant()
