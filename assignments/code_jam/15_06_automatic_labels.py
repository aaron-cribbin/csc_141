# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin

import plotly.express as px

from die import Die

die_1 = Die(8)
die_2 = Die(8)
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    print(results)

frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

fig - px.bar(x=poss_results, y=frequencies)
fig.show