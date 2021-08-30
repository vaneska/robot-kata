from src.robot import parts


class TestLeftArm:

    def test_initial_charge(self):
        arm = parts.LeftArm()

        assert arm._charge == 24

    def test_initial_turned_on(self):
        arm = parts.LeftArm()

        assert arm._turned_on_status is False


class TestRobotBus:

    def test_initial_turned_off(self):
        robot_bus = parts.RobotBus()

        assert robot_bus._turned_on_status is False