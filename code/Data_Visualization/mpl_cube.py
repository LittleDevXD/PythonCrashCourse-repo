import matplotlib.pyplot as plt

# Cubic Growth
x_values = range(0, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=5)

ax.set_title("Cubic Growth", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of Values", fontsize=14)

ax.axis([-100, 5100, -1000000000, 130000000000])

plt.show()
