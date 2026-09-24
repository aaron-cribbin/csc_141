# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

users = []
if users:
    for user in users:
        if user == "Admin":
            print("Welcome Admin, what would you like to change today?")
        else:
            print(f"Welcome {user}.")
else:
    print("We need to find more users!")