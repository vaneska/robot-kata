import math

from src.robot_v2.parts import Part, PartWithBattery
from typing import List


class DashBoard:

    def __init__(self, robot_part: Part):
        self.robot_part = robot_part

    def report_turned_on_status(self):
        return TurnedOnStatusReport(robot_part=self.robot_part).execute()


class TurnedOnStatusReport:
    OFFSET_SYMBOL = "\t"

    def __init__(self, robot_part: Part):
        self.robot_part = robot_part

    def execute(self):
        return "Turned on statuses:\n" + self._walk_through_parts(
            self.OFFSET_SYMBOL, [self.robot_part]
        )

    def _walk_through_parts(self, offset, parts: List[Part]) -> str:
        report = ""
        for part in parts:
            report += "{}{}: {}\n".format(offset, part.name, part.turned_on_status)
            if len(part.parts):
                report += self._walk_through_parts(offset+self.OFFSET_SYMBOL, part.parts)

        return report


class TotalRechargeCostReport:
    CHARGE_UNIT_COST = 0.2

    def __init__(self, robot_part: Part):
        self.robot_part = robot_part

    def execute(self):
        return "Total recharge cost is {}RUB".format(
            math.ceil(self._walk_through_parts([self.robot_part]) * self.CHARGE_UNIT_COST * 100)/100
        )

    def _walk_through_parts(self, parts: List[Part]) -> float:
        total_charge = 0.0
        for part in parts:
            if isinstance(part, PartWithBattery):
                total_charge += part.battery.MAX_CHARGE - part.battery.get_current_charge()
            if len(part.parts):
                total_charge += self._walk_through_parts(part.parts)

        return total_charge