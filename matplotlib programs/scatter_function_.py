import matplotlib.pyplot as plt

input_values = range(1,51)
output_values = [x**2 for x in input_values]

plt.style.use('classic')

fig, ax = plt.subplots()
ax.scatter(input_values[10], output_values[10], s=20, c='red')

ax.set_title("Squares")
ax.set_xlabel("Numbers")
ax.set_ylabel("Values")

ax.tick_params(axis='both', labelsize=12)

plt.show()
