import matplotlib.pyplot as plt

input_values = range(1,51)
output_values = [x**2 for x in input_values]

plt.style.use('classic')

fig, ax = plt.subplots()
ax.scatter(input_values, output_values, s=25, c=output_values, cmap=plt.cm.Blues)

ax.set_title("Squares")
ax.set_xlabel("Numbers")
ax.set_ylabel("Values")

ax.tick_params(axis='both', labelsize=12)
ax.axis([-1, 51, -100, 2600])

# plt.savefig('square_series.png', bbox_inches='tight')
plt.savefig('square_series.png')
plt.show()
