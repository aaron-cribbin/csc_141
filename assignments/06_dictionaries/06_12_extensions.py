# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

#Original Code
"""
favorite_numbers = {'Josh' : 27 , 
                    'Amy' : 30 , 
                    'Carl' : 2 , 
                    'Jamie' : 5 , 
                    'Riley' : 50}
#giving values to the numbers for the text
number_a = favorite_numbers['Josh']
number_b = favorite_numbers['Amy']
number_c = favorite_numbers['Carl']
number_d = favorite_numbers['Jamie']
number_e = favorite_numbers['Riley']

print(f"Josh's favorite number is {number_a}")
print(f"Amy's favorite number is {number_b}")
print(f"Carl's favorite number is {number_c}")
print(f"Jamie's favorite number is {number_d}")
print(f"Riley's favorite number is {number_e}")

"""

#Improved by cutting out almost the entire bottom half
favorite_numbers = {'Josh' : 27 , 
                    'Amy' : 30 , 
                    'Carl' : 2 , 
                    'Jamie' : 5 , 
                    'Riley' : 50}
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}")