from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import List


class Direction(Enum):
    U = "up"
    F = "forward"
    D = "down"
    B = "backward"


@dataclass
class Move:
    direction: str
    distance: int

    @staticmethod
    def from_string(value: str) -> Move:
        direction, distance = value.split(" ", maxsplit=1)
        return Move(Direction(direction), int(distance))


def answer_1(input: List[str]) -> int:
    horizontal_position: int = 0
    depth: int = 0

    normalized_list = map(Move.from_string, input)
    for move in normalized_list:
        if move.direction == Direction.F:
            horizontal_position += move.distance
        elif move.direction == Direction.D:
            depth += move.distance
        elif move.direction == Direction.U:
            depth -= move.distance

    return horizontal_position * depth


def answer_2(input: List[str]) -> int:
    horizontal_position: int = 0
    depth: int = 0
    aim: int = 0

    normalized_list = map(Move.from_string, input)
    for move in normalized_list:
        if move.direction == Direction.F:
            horizontal_position += move.distance
            depth += aim * move.distance
        elif move.direction == Direction.D:
            aim += move.distance
        elif move.direction == Direction.U:
            aim -= move.distance

    return horizontal_position * depth
