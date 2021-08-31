from src.robot_v2 import dashboard, parts


class TestTurnedOnStatusReport:
    report = dashboard.TurnedOnStatusReport(
        robot_part=parts.RobotBus(parts=[
            parts.LeftArm(),
            parts.RightHip(parts=[
                parts.RightThigh(parts=[parts.RightLowerLimb(
                    parts=[parts.RightFoot()]
                )])])
        ])
    )

    def test_report(self):
        orig_result = "Turned on statuses:\n\tRobot bus: OFF\n\t\tLeft arm: OFF\n\t\tRight hip: OFF\n\t\t\tRight thigh: OFF\n\t\t\t\tRight lower limb: OFF\n\t\t\t\t\tRight foot: OFF\n" # noqa

        result = self.report.execute()

        assert result == orig_result


class TestTotalRechargeCostReport:

    def test_initial_report(self):
        report = dashboard.TotalRechargeCostReport(
            robot_part=parts.RobotBus(parts=[
                parts.LeftArm(),
                parts.RightHip(parts=[
                    parts.RightThigh(parts=[parts.RightLowerLimb(
                        parts=[parts.RightFoot()]
                    )])])
            ])
        )
        orig_result = "Total recharge cost is 0.0RUB"  # noqa

        result = report.execute()

        assert result == orig_result

    def test_report_when_some_energy_was_wasted(self):
        report = dashboard.TotalRechargeCostReport(
            robot_part=parts.RobotBus(parts=[
                parts.LeftArm(
                    battery=parts.InternalBattery(current_charge=10)),
                parts.RightHip(parts=[
                    parts.RightThigh(parts=[parts.RightLowerLimb(
                        parts=[parts.RightFoot()]
                    )])])
            ])
        )
        orig_result = "Total recharge cost is 2.8RUB"  # noqa

        result = report.execute()

        assert result == orig_result
