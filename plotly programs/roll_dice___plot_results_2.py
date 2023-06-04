from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die = Die(4)
results = []
for i in range(1, 1001):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die.sides+1))

data = [Bar(x=x_values, y=frequencies)]

layout_config = [{'title': 'Rolling 4 sided die 1000 times'},
                 {'title': 'Results'},
                 {'title': 'Frequency of results'},]
layout = Layout(layout_config[0], xaxis=layout_config[1], yaxis=layout_config[2])
offline.plot({'data': data, 'layout': layout}, filename='D4.html')
