# task from Chapter_5 (pages 90-91)

import matplotlib.pyplot as plt
import numpy as np

temperatures = []
with open("temperatures.txt") as f:
    for row in f:
        temperatures.append(float(row.strip()))

print(temperatures[:15])
plt.plot(temperatures)

t_min, t_max = min(temperatures), max(temperatures)
print(f"minimum = {t_min} \nmaximum = {t_max}")

t_average = sum(temperatures) / len(temperatures)
print(f"average = {t_average:.{2}f}")

half_index = int(len(temperatures)/2)
t_median = sorted(temperatures)[half_index]
print(f"median = {t_median}")

# TODO: дополнительное задание стр 91

# let's play with matplotlib
# https://matplotlib.org/stable/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py

x = np.linspace(0, 2, 100)
# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
plt.show()
