# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open!")

place_1 = Restaurant("Koi (Hibachi)" , "Japanese")

place_2 = Restaurant("Texas Roadhouse" , "American")

place_3 = Restaurant("Olive Garden" , "Italian")

place_1.describe_restaurant()
place_2.describe_restaurant()
place_3.describe_restaurant()

place_1.open_restaurant()
place_3.open_restaurant()