# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

self = {'first_name' : 'Aaron' , 
        'last_name' : 'Cribbin' , 
        'Age' : 18 , 
        'Town' : 'Toms River'}

#Friend from a different example
friend_1 = {'first_name' : 'Collin' ,
            'last_name' : 'Tupper' , 
            'Age' :  18 , 
            'Town' : 'Toms River'}

#Another friend I don't see much
friend_2 = {'first_name' : 'Devlyn' ,
            'last_name' : 'Caine' , 
            'Age' :  18 , 
            'Town' : 'Toms River'}

people = [self , friend_1 , friend_2]
print("\nPeople:")
for person in people:
    print(f"\n- {person['first_name']} {person['last_name']}, Age: {person['Age']}, Town: {person['Town']}")  