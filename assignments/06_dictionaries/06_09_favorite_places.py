# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

#The first one is fully True
favorite_places = {
    'Aaron' : ['Home' , 'My Room' , "Chilli's"],
    'Teacher' : ['Office' , 'Classroom'], 
    'Friend' : ['Park' , 'My House' , 'Mall']}

for person, places in favorite_places.items():
    print(f"\n{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")