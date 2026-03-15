import random
from src.robot import Humanoid, Quadrotor, Driver

class Simulation:
    def __init__(self, n, grid_manager):
        """
        Handles the warehouse robot management simulation.

        :param n: Grid size.
        :param grid_manager: Instance of WarehouseGrid.
        """
        self.n = n
        self.grid_manager = grid_manager
        self.robots = []
        self._initialize_robots()

    def _initialize_robots(self):
        """Creates 2 * N robots with random types, starts, and ends."""
        robot_classes = [Humanoid, Quadrotor, Driver]
        num_robots = 2 * self.n

        for i in range(num_robots):
            robot_cls = random.choice(robot_classes)
            start = (random.randint(0, self.n - 1), random.randint(0, self.n - 1))
            end = (random.randint(0, self.n - 1), random.randint(0, self.n - 1))
            self.robots.append(robot_cls(i, start, end))

    def move_robot(self, robot):
        """Determines the next planned move for a robot towards its destination."""
        if robot.reached_destination():
            robot.next_pos = list(robot.current_pos)
            return

        next_x, next_y = list(robot.current_pos)

        # Move along X first, then Y
        if robot.current_pos[0] != robot.end_pos[0]:
            next_x += 1 if robot.end_pos[0] > robot.current_pos[0] else -1
        elif robot.current_pos[1] != robot.end_pos[1]:
            next_y += 1 if robot.end_pos[1] > robot.current_pos[1] else -1

        robot.next_pos = [next_x, next_y]

    def resolve_collisions(self):
        """Checks for robot collisions and applies resolution logic."""
        for i in range(len(self.robots)):
            for j in range(i + 1, len(self.robots)):
                r1 = self.robots[i]
                r2 = self.robots[j]

                # Check if they intend to move to the same spot and it's not their destination
                if r1.next_pos == r2.next_pos and r1.end_pos != r2.end_pos:
                    # Collision only matters if both are ground robots or both are aerial robots
                    # (Simplified from original: ground vs ground or aerial vs aerial)
                    if r1.is_aerial == r2.is_aerial:
                        d1 = r1.distance_to_destination()
                        d2 = r2.distance_to_destination()

                        if d1 < d2:
                            # r1 is closer, so r2 waits
                            r2.next_pos = list(r2.current_pos)
                        elif d2 < d1:
                            # r2 is closer, so r1 waits
                            r1.next_pos = list(r1.current_pos)
                        else:
                            # Equal distance, random choice
                            if random.choice([True, False]):
                                r1.next_pos = list(r1.current_pos)
                            else:
                                r2.next_pos = list(r2.current_pos)

    def run_step(self):
        """Executes one step of the simulation."""
        any_moving = False

        # 1. Plan next moves
        for robot in self.robots:
            if not robot.reached_destination():
                self.move_robot(robot)
                any_moving = True
            else:
                robot.next_pos = list(robot.current_pos)

        if not any_moving:
            return False

        # 2. Resolve collisions
        self.resolve_collisions()

        # 3. Apply moves
        for robot in self.robots:
            robot.current_pos = list(robot.next_pos)

        # 4. Visualize
        self.grid_manager.plot(self.robots)

        return True

    def run(self):
        """Runs the simulation until all robots reach their destinations."""
        # Initial plot
        print(f"Starting simulation with {len(self.robots)} robots...")
        self.grid_manager.plot(self.robots)

        step = 1
        while self.run_step():
            print(f"Step {step} completed.")
            step += 1

        print("Simulation finished! All robots reached their destinations.")
