# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

current_users = ["Admin","John Doe", "Jane Doe", "Joe Shmoe", "Mo Joe"]

#Lowercase
current_users = ["admin", "john doe", "jane doe", "joe shome", "mo joe"]


new_users = ["Collector", "JOHN DOE", "Buyer", "Stranger", "Mo Joe"]

for new_users in new_users:
    if new_users in current_users:
        print(f"Sorry {new_users}, this username is taken.")
    else:
        print(f"Welcome in {new_users}")