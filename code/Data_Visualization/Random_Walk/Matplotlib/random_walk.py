from random import choice

class RandomWalk:
    def __init__(self, max_x=500):
        self.max_x = max_x

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate and append x and y values"""
        while len(self.x_values) < self.max_x:
            x_walk = self._get_step()
            y_walk = self._get_step()

            # Reject movements that go nowhere
            if x_walk == 0 and y_walk == 0:
                continue

            # Calculate x and y values
            x = self.x_values[-1] + x_walk
            y = self.y_values[-1] + y_walk

            self.x_values.append(x)
            self.y_values.append(y)

    def _get_step(self):
        """Decide random steps"""
        direction = choice([-1, 1])
        step = choice([0, 2, 4, 8, 9, 10])
        walk = step * direction

        return walk