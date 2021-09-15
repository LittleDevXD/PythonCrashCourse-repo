import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # Ramdom Walk instance,
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Create visual fig
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(14,9), dpi=100)
    point_number = range(rw.max_x)
    ax.scatter(rw.x_values, rw.y_values, c=point_number, cmap=plt.cm.Purples, edgecolors='none', s=5, label='dots')
    ax.plot(rw.x_values, rw.y_values, c='orange', linewidth=0.5, label='straight line')

    # Distinct End Points
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    # Remove axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Set title of graph
    ax.set_title("Random Walk", fontsize=24)
    ax.legend()

    plt.show()

    break
    keep_going = input("Do you want to form another pattern? [Y/n]: ")
    if keep_going.lower() == "n":
        break