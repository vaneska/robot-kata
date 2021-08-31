from src.robot.dashboard import DashBoard
from src.robot import parts


class TestDashBoard:

    dashboard = DashBoard(robot_bus=parts.Trunk())

    def test_initial_turned_on_status_robot_report(self):
        """
         implement a function/method
         that navigates all the robot parts starting from robot bus,
         and reports the On/Off status of all robot parts,
         including the robot bus status.
         Report should have one line per robot part,
         and should use identation to visualise the tree structure
        """
        origin_report = "Turned on statuses:\n\tRobot bus: False\n\t\tShoulder: False\n\t\t\tLeft arm: False\n\t\tRight hip: False\n\t\t\tRight thigh: False\n\t\t\t\tRight lower limb: False\n\t\t\t\t\tRight foot: False\n" # noqa

        report = self.dashboard.report_turn_on_status()

        assert report == origin_report


class TestDashBoardTotalRechargeCostReport:
    """
    implement a function/method that navigates all the robot parts starting from robot bus,
     and calculates the total cost to re-charge all the internal batteries;
     the cost per 1000 Ah is £0.2.
    """
    dashboard = DashBoard(robot_bus=parts.Trunk())

    def test_initial_total_recharge_cost_report(self):
        """
        Отчет в начальном состоянии робота
        :return:
        """
        origin_report = "Total recharge cost is 0.0RUB"

        report = self.dashboard.report_total_recharge_cost()

        assert report == origin_report

    def test_when_some_energy_was_wasted(self):
        """
        Некоторое кол энергии потрачено
        """
        origin_report = "Total recharge cost is 2.8RUB"
        self.dashboard.trunk.shoulder.left_arm._charge = 10

        report = self.dashboard.report_total_recharge_cost()

        assert report == origin_report

