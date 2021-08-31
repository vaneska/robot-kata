from src.robot_v2 import parts


class TestBattery:

    battery = parts.InternalBattery()

    def test_max_charge(self):
        assert self.battery.MAX_CHARGE == 24

    def test_initial_charge(self):
        assert self.battery.current_charge() == 24


class TestLeftArm:

    arm = parts.LeftArm(
        battery=parts.InternalBattery(),
        turned_on_status=parts.TurnedOnStatus(False)
    )

    def test_initial_turned_on(self):
        """
        Finally the left arm also has a current On/Off switch status
        """
        assert not bool(self.arm._turned_on_status)
