# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

sandwich_orders = ['PB&J', 'BLT', 'Pannini', 'Ham & Cheese', 'Grilled Cheese', 'Pastrami', 'Pastrami', 'Pastrami']

finished_sandwiches = []

print("Sorry, we are out of Pastrami today.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    getting_sandwiches = sandwich_orders.pop()
    
    print(f'\nmaking your {getting_sandwiches.title()}')
    finished_sandwiches.append(getting_sandwiches)


print('\nThe following sandwiches are finished: ')
for finished_sandwiches in finished_sandwiches:
    print(finished_sandwiches.title())