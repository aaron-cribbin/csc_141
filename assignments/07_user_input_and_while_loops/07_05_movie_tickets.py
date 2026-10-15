# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

active = True
while active:
    age_of_person = input("How old are you? : ")
    if age_of_person == 'quit':
        active = False
    elif int(age_of_person) < 3:
        print("Your ticket is free!")
    elif int(age_of_person) < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")