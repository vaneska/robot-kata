from src.robot_v2 import dashboard, parts

class TestTurnedOnStatusReport:

    report = dashboard.TurnedOnStatusReport(
        robot_part= parts.RobotBus(parts=[
            parts.LeftArm(),
            parts.RightFoot(),
        ])
    )

    def test_report(self):
        orig_result = "Turned on statuses:\n\tRobot bus: OFF\n\t\tLeft arm: OFF\n\t\tRight foot: OFF\n" # noqa

        result = self.report.execute()

        assert result == orig_result
