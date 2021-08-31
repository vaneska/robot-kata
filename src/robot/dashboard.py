
from src.robot import parts
import math


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
        report += "\t\tRight hip: {}\n".format(
            self.robot_bus.right_hip._turned_on_status
        )
        report += "\t\t\tRight thigh: {}\n".format(
            self.robot_bus.right_hip.right_thigh._turned_on_status
        )
        report += "\t\t\tRight lower limb: {}\n".format(
            self.robot_bus.right_hip.right_lower_limb._turned_on_status
        )
        report += "\t\t\tRight foot: {}\n".format(
            self.robot_bus.right_hip.right_foot._turned_on_status
        )




        return report

    def report_total_recharge_cost(self):

        cost_per_unit = 0.2

        total_cost = cost_per_unit * (
                (self.robot_bus.left_arm._max_charge - self.robot_bus.left_arm._charge)
                +
                (self.robot_bus.right_hip.right_foot._max_charge - self.robot_bus.right_hip.right_foot._charge)
                +
                (self.robot_bus.right_hip.right_thigh._max_charge - self.robot_bus.right_hip.right_thigh._charge)
                +
                (self.robot_bus.right_hip.right_lower_limb._max_charge - self.robot_bus.right_hip.right_lower_limb._charge)
                +
                (self.robot_bus.right_hip._max_charge - self.robot_bus.right_hip._charge)
            )

        return "Total recharge cost is {}RUB".format(math.ceil(total_cost*100)/100)
