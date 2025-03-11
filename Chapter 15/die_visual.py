from die import Die
import plotly.express as px

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = list(range(2, max_result+1))
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1000 Times"
labels  = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=[1, 2, 3, 4, 5, 6], y=frequencies, title=title, labels=labels)
fig = px.bar(x=[1, 2, 3, 4, 5, 6], y=frequencies)
# Further customization of the chart
fig.update_layout (xaxis_dtick+1)
fig.show()

print(results)

