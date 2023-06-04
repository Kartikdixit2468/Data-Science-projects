from random import choice


class RandomWalk:
    """ A class to generate random walk like an confused ant. """

    def __init__(self, steps=5000):
        """
        Initializes the walk attributes of walk
        steps: Total number of steps.
        """

        self.steps = steps

        # Walk starts at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ Gives random walk points """
        while(len(self.x_values) < self.steps):

            x_direction = choice([-1, 1])
            x_dis = choice([0, 1, 2, 3, 4])
            x_steps = x_dis * x_direction


            y_direction = choice([-1, 1])
            y_dis = choice([0, 1, 2, 3, 4])
            y_steps = y_dis * y_direction

            if x_steps == 0 and y_steps == 0:
                continue

            x = self.x_values[-1] + x_steps
            y = self.y_values[-1] + y_steps

            self.x_values.append(x)
            self.y_values.append(y)


if __name__ == '__main__':
    pass
