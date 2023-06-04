import matplotlib.pyplot as plt

input_nums = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_nums, squares, linewidth=3)

ax.set_title("Squares", fontsize=30)
ax.set_xlabel("Numbers", fontsize=16)
ax.set_ylabel("Square Value", fontsize=16)

plt.show()
