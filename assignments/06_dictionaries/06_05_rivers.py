# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

rivers = {'mississippi' : 'United States' ,
          'nile' : 'Egypt' ,
          'amazon' : 'Brazil'}
for river, country in rivers.items():
    print(f"\nThe {river.title()} runs through {country.title()}.")
    print(f'\nRiver:{river}')
    print(f'\nCountry:{country}')
