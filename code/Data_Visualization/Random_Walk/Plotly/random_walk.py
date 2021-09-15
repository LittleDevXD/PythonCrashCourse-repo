from random import choice

class RandomWalk:
    def __init__(self, num_steps=500):
        self.num_steps = num_steps

        self.x_values = [0]
        self.y_values = [0]

    def predict_step(self):
        while len(self.x_values) < self.num_steps:
            x_walk = self._get_step()
            y_walk = self._get_step()

            x_next_step = self.x_values[-1] + x_walk # x next point
            y_next_step = self.y_values[-1] + y_walk # y next point

            self.x_values.append(x_next_step)
            self.y_values.append(y_next_step)

    def _get_step(self):
        # Return a random number
        direction = choice([-1, 1])
        step = choice([1, 2, 3, 4])
        walk = step * direction

        return walk