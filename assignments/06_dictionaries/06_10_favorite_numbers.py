# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

#Would Have made a pattern but I'm lazy and don't want to
favorite_numbers = {'Josh' : [27 , 13] , 
                    'Amy' : [30 , 45] , 
                    'Carl' : [2 , 18] , 
                    'Jamie' : [5 , 22] , 
                    'Riley' : [50 , 75]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")