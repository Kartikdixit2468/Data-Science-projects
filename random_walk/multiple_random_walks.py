# from tkinter import Y
import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_title('Random Walk')

    plt.show()

    choice = input("Generate a new random walk? (y/n) => ")
    if choice.lower() == 'y':
        continue
    break
