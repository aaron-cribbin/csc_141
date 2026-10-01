# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

#This one uses pre-made work from the book, I just add on to it
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

people = ['harry' , 'phil' , 'smith' , 'tom' , 'sarah']

for person in people:
    if person in favorite_languages.keys():
        print(f"\nThank you for taking the poll, {person.title()}!")
    else:
        print(f"\n{person.title()}, please take the poll!")