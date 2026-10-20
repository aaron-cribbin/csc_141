# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
tickets = 3
active = True
while active:
    age_of_person = input("Please enter your age or type 'quit' to exit : ")
    if age_of_person == 'quit':
        active = False
    elif int(age_of_person) < 3:
        print("Your ticket is free!")
        tickets -= 1
    elif int(age_of_person) < 13:
        print("Your ticket is $10.")
        tickets -= 1
    else:
        print("Your ticket is $15.")
        tickets -= 1

    if age_of_person == 'quit':
        break

    if tickets == 0:
        print("You cannot purchase more tickets.")
        break