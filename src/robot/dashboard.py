
from src.robot import parts


class DashBoard:

    def __init__(self, robot_bus: parts.RobotBus ):
        self.robot_bus = robot_bus

    def report_turn_on_status(self):

        report = "Turned on statuses:\n"
        report += "\tRobot bus: {}\n".format(
            self.robot_bus._turned_on_status
        )
        report += "\t\tLeft arm: {}\n".format(
            self.robot_bus.left_arm._turned_on_status
        )
        report += "\t\tRight foot: {}".format(
            self.robot_bus.right_foot._turned_on_status
        )

        return report

