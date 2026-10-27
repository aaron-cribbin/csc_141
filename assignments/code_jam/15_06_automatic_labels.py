# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
# THESE ARE ALL PAINS

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
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling two d8 1,000 times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.show()