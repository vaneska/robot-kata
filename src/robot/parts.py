
class LeftArm:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False


class RightFoot:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False


class RobotBus:

    def __init__(self):
        self._turned_on_status = False
        self.left_arm = LeftArm()
        self.right_foot = RightFoot()
