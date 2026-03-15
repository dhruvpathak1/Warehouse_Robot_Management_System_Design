import matplotlib.pyplot as plt

class WarehouseGrid:
    def __init__(self, n):
        """
        Initializes an N x N grid for robot simulation.

        :param n: Dimension of the square grid.
        """
        self.n = n
        self.color_map = {'humanoid': 'blue', 'quadrotor': 'red', 'driver': 'green'}

    def plot(self, robots):
        """
        Visualizes the current positions of robots on the grid.

        :param robots: List of robot objects.
        """
        fig, ax = plt.subplots(figsize=(self.n, self.n))
        ax.set_xlim(-1, self.n)
        ax.set_ylim(-1, self.n)
        ax.set_xticks(range(self.n))
        ax.set_yticks(range(self.n))
        ax.grid(True, linestyle='--', linewidth=0.5)
        ax.set_title("Warehouse Robot Navigation")

        added_labels = set()

        for robot in robots:
            x_init, y_init = robot.current_pos
            x_end, y_end = robot.end_pos
            robot_color = self.color_map.get(robot.type, 'black')

            # Draw path from current to destination
            ax.plot([x_init, x_end], [y_init, y_end], linestyle='--', color=robot_color, linewidth=1, alpha=0.5)

            # Mark current position (circle)
            label = robot.type if robot.type not in added_labels else None
            ax.scatter(x_init, y_init, color=robot_color, marker='o', label=label)
            if label:
                added_labels.add(robot.type)

            # Mark destination (square)
            ax.scatter(x_end, y_end, color=robot_color, marker='s')

        ax.legend()
        plt.show()
        plt.close(fig)
