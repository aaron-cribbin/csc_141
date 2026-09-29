# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

number = list(range(1,10))

ending = ""

for number in number:
    if number == 1:
        ending = "st"
    elif number == 2:
        ending = "nd"
    elif number == 3:
        ending = "rd"
    else:
        ending = "th"
    print(f"{number}{ending}")