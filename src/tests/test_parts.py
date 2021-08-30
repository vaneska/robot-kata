from src.robot import parts


class TestLeftArm:

    arm = parts.LeftArm()

    def test_initial_charge(self):
        """
        The left arm has a max charge (in Ampere Hour or Ah) of its internal 24KV battery.
        """
        assert self.arm._charge == 24

    def test_initial_turned_on(self):
        """
        Finally the left arm also has a current On/Off switch status
        """
        assert self.arm._turned_on_status is False


class TestRightFoot:

    arm = parts.RightFoot()

    def test_initial_charge(self):
        """
        The right foot has a max charge (in Ampere Hour or Ah) of its internal 24KV battery.
        """
        assert self.arm._charge == 24

    def test_initial_turned_on(self):
        """
        Finally the right foot also has a current On/Off switch status
        """
        assert self.arm._turned_on_status is False


class TestRobotBus:
    robot_bus = parts.RobotBus()

    def test_initial_turned_off(self):
        """
        Robot bus has an On/Off status like the left arm
        """
        assert self.robot_bus._turned_on_status is False

    def test_left_arm_connected_to_robot_bus(self):
        """
        the left arm is connected to the robot bus.
        """
        assert isinstance(self.robot_bus.left_arm, parts.LeftArm)