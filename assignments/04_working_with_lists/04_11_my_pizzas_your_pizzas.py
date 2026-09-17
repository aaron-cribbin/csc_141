# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

my_pizzas = ["Cheese", "Peperoni", "Mushrooms", "Peppers"]
friend_pizzas = my_pizzas[:]

my_pizzas.append('Sicilian')
friend_pizzas.append('Deep Dish')

print("My favorite pizzas are: ")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)