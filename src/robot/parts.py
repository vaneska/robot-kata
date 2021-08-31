
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


class RightThigh:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False


class RightLowerLimb:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False


class RightHip:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False
        self.right_foot = RightFoot()
        self.right_thigh = RightThigh()
        self.right_lower_limb = RightLowerLimb()


class RobotBus:

    def __init__(self):
        self._turned_on_status = False
        self.left_arm = LeftArm()
        self.right_hip = RightHip()
