from src.robot import parts


class TestLeftArm:

    def test_initial_charge(self):
        arm = parts.LeftArm()

        assert arm.charge == 24

    def test_initial_turned_on(self):
        arm = parts.LeftArm()

        assert arm._turned_on_status is False
