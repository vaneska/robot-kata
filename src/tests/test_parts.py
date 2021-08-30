from src.robot import parts


class TestLeftArm:

    def test_initial_charge(self):
        arm = parts.LeftArm()

        assert arm.charge == 24
