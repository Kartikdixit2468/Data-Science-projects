import matplotlib.pyplot as plt

input_values = range(1,21)
output_values = [x**3 for x in input_values]

plt.style.use('classic')

fig, ax = plt.subplots()
ax.scatter(input_values, output_values, s=30, c=output_values, cmap=plt.cm.Greens)

ax.set_title('Cubes')
ax.set_xlabel('Numbers')
ax.set_ylabel('Values')
ax.axis([-1, 21,-500 ,8500])

plt.savefig('Cube_graph.png')
plt.show()
