import re

from collections import deque
from dataclasses import InitVar
from dataclasses import dataclass
from dataclasses import field
from itertools import filterfalse
from itertools import zip_longest
from typing import Deque
from typing import Iterable
from typing import List
from typing import Set
from typing import Tuple


@dataclass
class Board:
    lines: InitVar

    combinations: List[Set[int]] = field(init=False)
    numbers: Set[int] = field(init=False)
    marked: Set[int] = field(init=False)
    winner: Set[int] = field(init=False, default=None)

    def __post_init__(self, lines: Tuple[str]):
        self.combinations = []
        self.numbers = set()
        self.marked = set()

        # build position matrix
        positions = [[] for _ in range(5)]
        for y, line in enumerate(lines):
            for x, number in enumerate(re.split(r"\s+", line.strip())):
                self.numbers.add(int(number))
                positions[int(y)].append(int(number))

        # build winning combinations set
        for n in range(5):
            self.combinations.append(set([col[n] for col in positions]))
            self.combinations.append(set([row for row in positions[n]]))

    def has_bingo(self) -> bool:
        # quick exit in case we won
        if self.winner is not None:
            return True

        # we can't win with less than 5 numbers
        if len(self.marked) > 4:
            for combination in self.combinations:
                if combination.issubset(self.marked):
                    self.winner = combination
                    return True

        return False


def group(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def walk(boards: Iterable[Board], numbers: Deque[int], continue_until_end: bool = False) -> Tuple[Board, int]:
    last_board, last_number = None, None

    try:
        while numbers:
            number = numbers.popleft()
            for board in filter(lambda b: b.winner is None, boards):
                if number in board.numbers:
                    board.marked.add(number)
                    if board.has_bingo():
                        last_board = board
                        last_number = number

                        if not continue_until_end:
                            raise StopIteration
    except StopIteration:
        pass

    if last_board is not None and last_number is not None:
        return last_board, last_number

    raise RuntimeError("No winning combinations found!")


def solution_1(input: List[str]) -> int:
    numbers = deque([int(number) for number in input.pop(0).split(",")])
    boards = [Board(lines) for lines in group(filterfalse(lambda e: e == "", input[1:]), 5)]

    winning_board, winning_number = walk(boards, numbers)
    result = sum(winning_board.numbers.difference(winning_board.marked)) * winning_number

    return result


def solution_2(input: List[str]) -> int:
    numbers = deque([int(number) for number in input.pop(0).split(",")])
    boards = [Board(lines) for lines in group(filterfalse(lambda e: e == "", input[1:]), 5)]

    winning_board, winning_number = walk(boards, numbers, True)
    result = sum(winning_board.numbers.difference(winning_board.marked)) * winning_number

    return result
