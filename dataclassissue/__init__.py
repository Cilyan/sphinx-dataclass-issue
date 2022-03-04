from dataclasses import dataclass


@dataclass
class IssueDemo:
    var1: int
    var2: str


class IssueDemo2:
    def __init__(self, var1: int, var2: str) -> None:
        self.var1 = var1
        self.var2 = var2
