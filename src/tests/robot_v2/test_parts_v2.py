from src.robot_v2 import parts


class TestBattery:

    battery = parts.InternalBattery()

    def test_max_charge(self):
        assert self.battery.MAX_CHARGE == 24

    def test_initial_charge(self):
        assert self.battery.get_current_charge() == 24


class TestPart:

    part = parts.Part()

    def test_initial_turned_on(self):
        assert not bool(self.part.turned_on_status)

    def test_initial_parts(self):
        assert len(self.part.parts) == 0

    def test_name_attr(self):
        assert self.part.name == 'Part'


class TestPartWithBattery:

    part = parts.PartWithBattery()

    def test_initial_battery(self):
        assert isinstance(self.part.battery, parts.InternalBattery)

    def test_name_attr(self):
        assert self.part.name == 'PartWithBattery'

class TestRobotBus:

    robot_bus = parts.RobotBus(
        parts=[parts.LeftArm(), parts.RightFoot()]
    )

    def test_initial_turned_on(self):
        assert not bool(self.robot_bus.turned_on_status)

    def test_all_parts_connected(self):
        part_types = [parts.LeftArm, parts.RightFoot]

        assert len(part_types) == len(self.robot_bus.parts)

        i = 0
        for part_type in part_types:
            assert isinstance(self.robot_bus.parts[i], part_type)
            i += 1
