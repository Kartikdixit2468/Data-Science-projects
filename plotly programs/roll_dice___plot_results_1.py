from die import Die
from plotly.graph_objects import Bar, Layout
from plotly import offline

die = Die(6)
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

x_config = {'title': 'Results'}
y_config = {'title': 'Frequency of results'}

layout = Layout(title="Rolling a D6 1000 times.", xaxis=x_config, yaxis=y_config)
offline.plot({'data': data, 'layout': layout}, filename='D6.html')
