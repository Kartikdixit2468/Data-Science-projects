import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_num = range(rw.steps)
    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    ax.set_title('Random Walk', fontsize=50)

    ax.scatter(0, 0, s=100, c='red', edgecolors='none')
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=100, c='green', edgecolors='none')

    # To set visibility False of x and y axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()

    choice = input("Generate a new random walk? (y/n) => ")
    if choice.lower() == 'n':
        break
