# This is my work (^_^)

list= ["Ryan Gosling", "Markiplier", "Weird Al Yankovic", "Mathew McConaughey"]

list.insert(0, "Tom Holland")
list.insert(3, "Chris Pratt")
list.append("Sigourney Weaver")

list_2= ["Ryan Gosling", "Markiplier", "Weird Al Yankovic", "Mathew McConaughey", "Tom Holland", "Chris Pratt", 
         "Sigourney Weaver"]

print("Sorry, but due to unforeseen circumstances, I can only invite two people to the dinner party.")


popped_guest= list_2.pop()
popped_guest_2= list_2.pop()
popped_guest_3= list_2.pop()
popped_guest_4= list_2.pop()
popped_guest_5= list_2.pop()

print(f"Sorry {popped_guest}, but I can't invite you to the dinner party.")
print(f"Sorry {popped_guest_2}, but I can't invite you to the dinner party.")
print(f"Sorry {popped_guest_3}, but I can't invite you to the dinner party.")
print(f"Sorry {popped_guest_4}, but I can't invite you to the dinner party.")
print(f"Sorry {popped_guest_5}, but I can't invite you to the dinner party.")

print(f"{list_2[0]}, you are still invited to the dinner party.")
print(f"{list_2[1]}, you are still invited to the dinner party.")

del list_2[0]
del list_2[0]
print(list_2)

# These two are actually shipped online btw <3