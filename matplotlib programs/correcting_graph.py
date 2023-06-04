import matplotlib.pyplot as plt

input_nums = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_nums, squares, linewidth=3)
plt.show()
