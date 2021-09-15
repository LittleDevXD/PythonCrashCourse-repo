import matplotlib.pyplot as plt

# Input values
input_values = [1, 2, 3, 4, 5, 6]

# Output values
squares = [1, 4, 9, 16, 25, 36]

# Built-in style
plt.style.use('ggplot')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Title of graph
ax.set_title("Square Numbers", fontsize=24)

# Label of x-axis
ax.set_xlabel("Values", fontsize=14)

# Label of y-axis
ax.set_ylabel("Squares of values", fontsize=14)

# Set size of tick labels
ax.tick_params(axis="both", labelsize=14)



plt.show()
