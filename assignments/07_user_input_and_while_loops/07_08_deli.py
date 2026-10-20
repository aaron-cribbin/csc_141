# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

sandwich_orders = ['PB&J', 'BLT', 'Pannini', 'Ham & Cheese', 'Grilled Cheese']

finished_sandwiches = []

while sandwich_orders:
    getting_sandwiches = sandwich_orders.pop()
    
    print(f'making your {getting_sandwiches.title()}')
    finished_sandwiches.append(getting_sandwiches)


print('\nThe following sandwiches are finished: ')
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title())