# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
# THESE ARE ALL PAINS
import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()
results = []

for roll_num in range(20):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling three d6 20 times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.show()