# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

from die import Die

die = Die(8)
results = []

for roll_num in range(10):
    result = die.roll()
    results.append(result)
    print(results)