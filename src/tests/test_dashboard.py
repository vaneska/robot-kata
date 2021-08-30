from src.robot.dashboard import DashBoard
from src.robot import parts


class TestDashBoard:

    dashboard = DashBoard(robot_bus=parts.RobotBus())

    def test_initial_turned_on_status_robot_report(self):
        """
         implement a function/method
         that navigates all the robot parts starting from robot bus,
         and reports the On/Off status of all robot parts,
         including the robot bus status.
         Report should have one line per robot part,
         and should use identation to visualise the tree structure
        """
        origin_report = "Turned on statuses:\n\tRobot bus: False\n\t\tLeft arm: False\n\t\tRight foot: False" # noqa

        report = self.dashboard.report_turn_on_status()

        assert report == origin_report
