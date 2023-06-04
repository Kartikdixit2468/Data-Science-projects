from shutil import which
import matplotlib.pyplot as plt

fonts_available = ['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']

input_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

plt.style.use(fonts_available[17])
fig, ax = plt.subplots()
ax.plot(input_nums, squares, linewidth=3)

ax.set_title("Squares", fontsize=30)
ax.set_xlabel("Numbers", fontsize=16)
ax.set_ylabel("Values", fontsize=16)

ax.tick_params(axis='both', which='major', labelsize=15)

plt.show()
