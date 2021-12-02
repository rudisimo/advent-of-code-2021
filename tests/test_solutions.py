import importlib

from typing import List

import pytest


def solve_puzzle(day: int, puzzle: int, input: List[str]) -> str:
    try:
        solver = getattr(importlib.import_module(f"aoc.day_{day:0{2}}"), f"answer_{puzzle}")
    except (AttributeError, ModuleNotFoundError) as e:
        raise NotImplementedError(f"no implementation: aoc.day_{day:0{2}}:answer_{puzzle} ({e})")
    else:
        return str(solver(input))


@pytest.mark.parametrize(
    "day,part",
    [
        pytest.param(1, 1, id="1-1"),
        pytest.param(1, 2, id="1-2"),
    ],
)
def test_should_solve_puzzle(load_fixture, day: int, part: int) -> None:
    try:
        fixtures = load_fixture(day, part)
        for (input, expected) in fixtures:
            assert solve_puzzle(day, part, input) == expected
    except (FileNotFoundError, NotImplementedError) as e:
        pytest.skip(f"Skipping {day}-{part}: ({e})")
