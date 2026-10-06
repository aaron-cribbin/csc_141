# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

dog_1 = {'name' : 'Mushi' ,
            'breed' : 'German Shepherd' ,
            'owner' : 'John Doe'}

cat_1 = {'name' : 'Bingus' ,
            'kind' : 'Calico' ,
            'owner' : 'Jane Smith'}

dog_2 = {'name' : 'Pony Boy' ,
            'breed' : 'Golden Retriever' ,
            'owner' : 'Clark'}

cat_2 = {'name' : 'Goober' ,
            'kind' : 'Tabby' ,
            'owner' : 'Kevin Johnson'}

snake = {'name' : 'Sly' ,
            'kind' : 'Python' ,
            'owner' : 'Parker Ginnis'}

pets = [dog_1 , cat_1 , dog_2 , cat_2 , snake]
print("\nPets:")
for pet in pets:
    if 'breed' in pet:
        print(f"\n- {pet['name']}, Breed: {pet['breed']}, Owner: {pet['owner']}")
    else:
        print(f"\n- {pet['name']}, Kind: {pet['kind']}, Owner: {pet['owner']}")

#God, I hate thinking of names. Both for Pets and People