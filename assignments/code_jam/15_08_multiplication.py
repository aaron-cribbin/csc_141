# This is my work (^_^)
# All of this is written by me
# Aaron Cribbin
import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()
results = []

for roll_num in range(100):
    result = die_1.roll() * die_2.roll()
    results.append(result)
    print(results)

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of rolling two d6 100 times"
labels = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title = title, labels = labels)
fig.show()