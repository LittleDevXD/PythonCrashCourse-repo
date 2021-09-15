import matplotlib.pyplot as plt

# input values
input_values = range(1, 1001)

# output_values
output_values = [x**2 for x in input_values]

# built-in style
plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.scatter(input_values, output_values, c=output_values, cmap= plt.cm.Purples, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Values", fontsize= 14)
ax.set_ylabel("Squares of values", fontsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 11000_00])

plt.savefig("square_plot.png", bbox_inches='tight')