# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

location_poll = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? : ")
    response = input("If you could visit one place in the world, where would you go? : ")
    location_poll[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) : ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in location_poll.items():
    print(f"{name} would like to visit {response}.")