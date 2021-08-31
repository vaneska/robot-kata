from src.robot_v2.parts import Part
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