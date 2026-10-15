# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

pizzas = True
while pizzas:
    topping = input("What topping would you like on your pizza? : ")
    if topping == 'quit':
        pizzas = False
    else:
        print(f'We will add {topping} to your pizza!')