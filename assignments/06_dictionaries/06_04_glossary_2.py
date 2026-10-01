# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

glossary = {'elif_block' : 'a block with the same functions as an else block.' , 
            'lists' : 'items that are listed within square brackets, []' , 
            'tuple' : 'a list, but instead of square brackets, it is parenthesis, ()' ,
            'loop' : 'code that is run multiple times with different values all at once' ,
            'popping' : 'when you remove the end value of a list with the "pop()" command' ,
            'variable' : 'a name that is used to store a value in a program' ,
            'dictionary' : 'a data structure that stores key-value pairs,' ,
            'function' : 'a block of code that performs a specific task and can be called multiple times in a program' ,
            'parameter' : 'a value that is passed into a function to be used within the function' ,
            'argument' : 'a value that is passed into a function when it is called'}

for key, value in glossary.items():
    print(f"\n{key.title()} - {value}")