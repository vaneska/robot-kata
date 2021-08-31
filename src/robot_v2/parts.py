class TurnedOnStatus:

    def __init__(self, status: bool):
        self.status = status

    def __str__(self):
        if self.status :
            return "ON"
        else :
            return "OFF"

    def __bool__(self):
        return self.status


class InternalBattery:

    MAX_CHARGE = 24

    def __init__(self):
        self._current_charge = self.MAX_CHARGE

    def current_charge(self):
        return self._current_charge


class LeftArm:

    def __init__(
            self,
            battery: InternalBattery = InternalBattery(),
            turned_on_status: TurnedOnStatus = TurnedOnStatus(False)
    ):
        self.battery = battery
        self._turned_on_status = turned_on_status


class RobotBus:

    def __init__(
            self,
            left_arm: LeftArm,
            turned_on_status: TurnedOnStatus = TurnedOnStatus(False)
    ):
        self._turned_on_status = turned_on_status
        self.left_arm = left_arm