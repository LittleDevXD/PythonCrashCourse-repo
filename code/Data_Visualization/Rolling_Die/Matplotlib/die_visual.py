import matplotlib.pyplot as plt
from die import Die

# Create dice instances
die1 = Die(8)
die2 = Die(8)

# Calculate the results
results = []
roll_nums = 50000
for roll_num in range(roll_nums):
    result = die1.roll() + die2.roll()
    results.append(result)

frequencies = []
max_sides = die1.num_sides + die2.num_sides
for value in range(1, max_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
plt.style.use('seaborn') # Use a built-in style

fig, ax = plt.subplots(figsize=(16, 9))

x_values = list(range(1, max_sides+1))
ax.bar(x_values, frequencies, color='green') # Bar
ax.plot(x_values, frequencies, c='red') # Plot
ax.scatter(x_values, frequencies, c='blue', s=100) # Scatter

ax.set_title(f"Result of rolling D{die1.num_sides} and D{die2.num_sides} die {roll_nums} times", 
            fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Frequencies of values", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()