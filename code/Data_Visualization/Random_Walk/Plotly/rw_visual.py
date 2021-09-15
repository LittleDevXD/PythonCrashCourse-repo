from plotly.graph_objs import Scatter, Bar, Layout
from plotly import offline
from random_walk import RandomWalk

rw = RandomWalk()
rw.predict_step()

x_values = rw.x_values
y_values = rw.y_values
data = [Scatter(x=x_values, y=y_values)] # Scatter

x_axis = {'title' : ""}
y_axis = {'title' : ""}
my_layout = Layout(title="Steps of a cell moving in water", xaxis=x_axis, yaxis=y_axis) # Layout

offline.plot({'data':data, 'layout':my_layout}, filename="RandomWalk.html")