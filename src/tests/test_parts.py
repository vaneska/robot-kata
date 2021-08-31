from src.robot import parts


class TestLeftArm:

    arm = parts.LeftArm()

    def test_max_charge(self):
        """
        В левой руке может быть максимально 24Ah заряда
        """
        assert self.arm._max_charge == 24

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


class TestShoulder:

    shoulder = parts.Shoulder()

    def test_max_charge(self):
        assert self.shoulder._max_charge == 24

    def test_initial_charge(self):
        assert self.shoulder._charge == 24

    def test_initial_turned_on(self):
        assert self.shoulder._turned_on_status is False

    def test_left_arm_connected_to_robot_bus(self):
        """
        the left arm is connected to the robot bus.
        """
        assert isinstance(self.shoulder.left_arm, parts.LeftArm)


class TestRightFoot:

    arm = parts.RightFoot()

    def test_max_charge(self):
        """
        В правой ступне может быть максимально 24Ah заряда
        """
        assert self.arm._max_charge == 24

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


class TestRightThigh:

    right_thigh = parts.RightThigh()

    def test_max_charge(self):
        assert self.right_thigh._max_charge == 24

    def test_initial_charge(self):
        assert self.right_thigh._charge == 24

    def test_initial_turned_on(self):
        assert self.right_thigh._turned_on_status is False

    def test_right_lower_limb_connected_to_robot_bus(self):
        """
        the right lower limb is connected to the robot bus too.
        """
        assert isinstance(self.right_thigh.right_lower_limb, parts.RightLowerLimb)


class TestRightLowerLimb:

    right_lower_limb = parts.RightLowerLimb()

    def test_max_charge(self):
        assert self.right_lower_limb._max_charge == 24

    def test_initial_charge(self):
        assert self.right_lower_limb._charge == 24

    def test_initial_turned_on(self):
        assert self.right_lower_limb._turned_on_status is False

    def test_right_foot_connected_to_robot_bus(self):
        """
        the right foot is connected to the robot bus too.
        """
        assert isinstance(self.right_lower_limb.right_foot, parts.RightFoot)


class TestRightHip:

    right_hip = parts.RightHip()

    def test_max_charge(self):
        assert self.right_hip._max_charge == 24

    def test_initial_charge(self):
        assert self.right_hip._charge == 24

    def test_initial_turned_on(self):
        assert self.right_hip._turned_on_status is False

    def test_right_thigh_connected_to_robot_bus(self):
        """
        the right thigh is connected to the robot bus too.
        """
        assert isinstance(self.right_hip.right_thigh, parts.RightThigh)


class TestRobotBus:
    robot_bus = parts.Trunk()

    def test_initial_turned_off(self):
        """
        Robot bus has an On/Off status like the left arm
        """
        assert self.robot_bus._turned_on_status is False

    def test_right_hip_connected_to_robot_bus(self):
        """
        the right lower limb is connected to the robot bus too.
        """
        assert isinstance(self.robot_bus.right_hip, parts.RightHip)

    def test_shoulder_connected_to_robot_bus(self):
        """
        the right shoulder is connected to the robot bus too.
        """
        assert isinstance(self.robot_bus.shoulder, parts.Shoulder)