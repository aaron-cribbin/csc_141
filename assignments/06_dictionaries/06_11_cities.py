# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

cities = {
    'New York' : {'Country' : 'United States' ,
                   'Population' : 8419600 ,
                   'Fact' : 'New York City is one of the most known cities in the world.'},
    'Tokyo' : {'Country' : 'Japan' ,
               'Population' : 13929286 ,
               'Fact' : 'Tokyo is the most populated city in the world.'},
    'Rome' : {'Country' : 'Italy' ,
              'Population' : 2873000 ,
                'Fact' : 'Rome is known for its ancient history and architecture.'}
}

for city, info in cities.items():
    print(f"\n{city} is in {info['Country']}.")
    print(f"It has a population of {info['Population']}.")
    print(f"Fun Fact: {info['Fact']}")