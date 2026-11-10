# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def tables(self):
        print(f"{self.restaurant_name} has served {self.number_served} tables.")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, additional_tables):
        self.number_served += additional_tables

restaurant = Restaurant("Koi (Hibachi)" , "Japanese")
restaurant.set_number_served(5)
restaurant.increment_number_served(18)
restaurant.tables()