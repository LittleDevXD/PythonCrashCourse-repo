from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Setup Dice
die1 = Die(8)
die2 = Die(8)

roll_nums = 5000
results = [die1.roll() + die2.roll() for roll_num in range(roll_nums)]

# Calculate the results
max_num = die1.num_sides + die2.num_sides
frequencies = [results.count(value) for value in range(1, max_num+1)]

# Visualize the results
x_values = list(range(1, max_num+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title':"Result", 'dtick':1}
y_axis_config = {'title':"Frequency of Result"}
my_layout = Layout(title=f"Result of rolling D{die1.num_sides} and D{die2.num_sides} dice {roll_nums} times", 
                xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data':data, 'layout':my_layout}, filename="d6.html")