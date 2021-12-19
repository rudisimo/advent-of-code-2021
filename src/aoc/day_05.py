from dataclasses import InitVar
from dataclasses import dataclass
from dataclasses import field
from typing import Iterable
from typing import List
from typing import Tuple


@dataclass(frozen=True)
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_straight(self) -> bool:
        return self.x1 == self.x2 or self.y1 == self.y2

    def as_tuple(self) -> Tuple[int, int, int, int]:
        return self.x1, self.y1, self.x2, self.y2


@dataclass
class Diagram:
    input_lines: InitVar

    lines: List[Line] = field(init=False, default_factory=list)
    points: List[List[int]] = field(init=False, default_factory=list)

    def __post_init__(self, input_lines: Iterable[Tuple[List[str]]]):
        width, height = 0, 0

        # generate lines
        for (line_start, line_end) in input_lines:
            line = Line(*(map(int, line_start)), *(map(int, line_end)))
            width = max(width, max(line.x1, line.x2) + 1)
            height = max(height, max(line.y1, line.y2) + 1)
            self.lines.append(line)

        # generate empty point map
        self.points = [[0 for _ in range(width)] for _ in range(height)]

    def plot_point(self, x: int, y: int):
        self.points[y][x] += 1


def walk(lines: Iterable[Line]) -> Iterable[Tuple[int, int]]:
    for line in lines:
        # extract coordinates
        x0, y0, x1, y1 = line.as_tuple()

        # calculate initial deltas
        dx = abs(x1 - x0)
        sx = 1 if x0 < x1 else -1
        dy = -abs(y1 - y0)
        sy = 1 if y0 < y1 else -1

        # use integer incremental error to perform octant line draws
        # source: (https://en.wikipedia.org/wiki/Bresenham's_line_algorithm#All_cases)
        err = dx + dy
        while True:
            yield x0, y0
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy


def solution_1(input: List[str]) -> int:
    normalized_lines = [(s.split(","), e.split(",")) for d in input for s, e in [d.split(" -> ")]]
    diagram = Diagram(normalized_lines)

    for x, y in walk(filter(lambda l: l.is_straight(), diagram.lines)):
        diagram.plot_point(x, y)
    results = len([v for y in diagram.points for v in y if v > 1])

    return results


def solution_2(input: List[str]) -> int:
    normalized_lines = [(s.split(","), e.split(",")) for d in input for s, e in [d.split(" -> ")]]
    diagram = Diagram(normalized_lines)

    for x, y in walk(diagram.lines):
        diagram.plot_point(x, y)
    results = len([v for y in diagram.points for v in y if v > 1])

    return results
