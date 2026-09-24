# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

#Inequalities

color = "Blue"

if color != "Blue":
    print("The color cannot be Blue!")

if color != "Red":
    print("The color can be Red")

#lower() method

game = "Deadlock"

print(game.lower() == "Deadlock")

print(game.lower() == "deadlock")

#Numerical Tests

# Equal To
value_0 = 5

print(value_0 == 5)

print(value_0 == 3)

# Not Equal To
value_1 = 7

print(value_1 != 7)

print(value_1 != 9)
# > 
value_2 = 29

print(value_2 > 15)

print(value_2 > 99)

# <
value_3 = 50

print(value_3 < 100)

print(value_3 < 25)

# >=
value_4 = 15

print(value_4 >= 15)

print(value_4 >= 20)

# <=
value_5 = 30

print(value_5 <= 50)

print(value_5 <= 20)

#and/or Keywords

age_0 = 18
age_1 = 25

#and
print(age_0 >= 18 and age_1 >= 20)

print(age_0 >= 20 and age_1 >= 18)

#or
print(age_0 >= 18 or age_1 >= 26)

print(age_0 >= 19 or age_1 >= 26)

#If something is on a list

dyes = ['Aqua', 'Lime', 'Yellow', 'Red']

print('Aqua' in dyes)

print('Orange' in dyes)

#If something isn't on a list

toppings = ['Sprinkles', 'M&Ms', 'Cherries']
extra_0 = "Fudge"
extra_1 = "Cherries"

if extra_0 not in toppings:
    print(extra_0 + ' is not on this sunday')

if extra_1 not in toppings:
    print(extra_1 + ' should be on this sunday')