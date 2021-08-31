from __future__ import annotations
from typing import List, Optional


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


class Part:

    def __init__(
            self,
            parts: Optional[List[Part]] = None,
            turned_on_status: TurnedOnStatus = TurnedOnStatus(False)
    ):
        self.parts = parts or []
        self.turned_on_status = turned_on_status
        self.name = "Part"


class PartWithBattery:

    def __init__(
            self,
            parts: Optional[List[Part]] = None,
            battery: InternalBattery = InternalBattery(),
            turned_on_status: TurnedOnStatus = TurnedOnStatus(False)
    ):
        self.parts = parts or []
        self.battery = battery
        self.turned_on_status = turned_on_status
        self.name = "PartWithBattery"


class LeftArm(Part):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Left arm"


class RightFoot(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Right foot"


class RobotBus(Part):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Robot bus"
