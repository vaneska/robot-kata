
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


class LeftArm:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = TurnedOnStatus(False)


class Shoulder:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False
        self.left_arm = LeftArm()


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
        self.right_lower_limb = RightLowerLimb()


class RightLowerLimb:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False
        self.right_foot = RightFoot()


class RightHip:

    def __init__(self):
        self._max_charge = 24
        self._charge = self._max_charge
        self._turned_on_status = False
        self.right_thigh = RightThigh()


class Trunk:

    def __init__(self):
        self._turned_on_status = False
        self.right_hip = RightHip()
        self.shoulder = Shoulder()

