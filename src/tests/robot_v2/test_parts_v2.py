from src.robot_v2 import parts


class TestBattery:

    battery = parts.InternalBattery()

    def test_max_charge(self):
        assert self.battery.MAX_CHARGE == 24

    def test_initial_charge(self):
        assert self.battery.current_charge() == 24


class TestLeftArm:

    arm = parts.LeftArm()

    def test_initial_turned_on(self):
        assert not bool(self.arm._turned_on_status)


class TestRobotBus:

    robot_bus = parts.RobotBus(
        left_arm=parts.LeftArm()
    )

    def test_initial_turned_on(self):
        assert not bool(self.robot_bus._turned_on_status)

    def test_left_arm_connected(self):
        assert isinstance(self.robot_bus.left_arm, parts.LeftArm)