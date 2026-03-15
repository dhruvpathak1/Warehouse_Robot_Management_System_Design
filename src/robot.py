import math

class Robot:
    def __init__(self, robot_id, robot_type, start_pos, end_pos):
        """
        Base class for all robots.

        :param robot_id: Unique identifier for the robot.
        :param robot_type: String indicating the type of robot.
        :param start_pos: Tuple (x, y) of the starting position.
        :param end_pos: Tuple (x, y) of the destination.
        """
        self.robot_id = robot_id
        self.type = robot_type
        self.current_pos = list(start_pos)
        self.end_pos = list(end_pos)
        self.next_pos = list(start_pos)
        self.is_aerial = (robot_type == 'quadrotor')

    def distance_to_destination(self, pos=None):
        """Calculates Euclidean distance to destination from a given position (defaults to current)."""
        if pos is None:
            pos = self.current_pos
        return round(math.sqrt(((self.end_pos[1] - pos[1])**2) + ((self.end_pos[0] - pos[0])**2)), 1)

    def reached_destination(self):
        """Checks if the robot has reached its destination."""
        return self.current_pos == self.end_pos

    def __repr__(self):
        return f"{self.type.capitalize()}Robot(ID={self.robot_id}, Current={self.current_pos}, Target={self.end_pos})"

class Humanoid(Robot):
    def __init__(self, robot_id, start_pos, end_pos):
        super().__init__(robot_id, 'humanoid', start_pos, end_pos)

class Quadrotor(Robot):
    def __init__(self, robot_id, start_pos, end_pos):
        super().__init__(robot_id, 'quadrotor', start_pos, end_pos)

class Driver(Robot):
    def __init__(self, robot_id, start_pos, end_pos):
        super().__init__(robot_id, 'driver', start_pos, end_pos)
