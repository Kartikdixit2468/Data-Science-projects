from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die_1 = Die()
die_2 = Die()

results = []
for i in range(1, 1001):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
for value in range(2, die_1.sides + die_2.sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, die_1.sides + die_2.sides + 1))

layout_config = [{'title': 'Rolling 2 dices at a time 1000 times'},
                 {'title': 'Frequency of results'},
                 {'title': 'Results', 'dtick': 1}]

data = [Bar(x=x_values, y=frequencies)]
layout = Layout(layout_config[0], xaxis=layout_config[2], yaxis=layout_config[1])

offline.plot({'data': data, 'layout': layout}, filename='2_dice_plot.html')
