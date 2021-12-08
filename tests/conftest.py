import importlib

from glob import glob
from pathlib import Path
from typing import List
from typing import Optional
from typing import Tuple

import pytest


@pytest.fixture
def solve_puzzle():
    def wrapper(day: int, part: int, input: List[str]) -> Optional[str]:
        try:
            solver = getattr(importlib.import_module(f"aoc.day_{day:0{2}}"), f"answer_{part}")
        except (AttributeError, ModuleNotFoundError) as e:
            raise NotImplementedError(f"aoc.day_{day:0{2}}.answer_{part}: {e}")
        else:
            return str(solver(input))

    return wrapper


@pytest.fixture
def load_fixture():
    def wrapper(day: int, part: int, pattern: str = "*") -> Tuple[List[str], Optional[str]]:
        fixtures = glob(f"{Path().absolute()}/tests/fixtures/{day:0{2}}-{pattern}.txt")
        for fixture in fixtures:
            try:
                with open(fixture) as f:
                    samples = f.read().split("---------------------\n")
                    yield (samples[0].splitlines(), samples[part].strip())
            except (IndexError):
                yield ([], None)
        if not fixtures:
            raise FileNotFoundError(f"no fixtures: tests/fixtures/{day:0{2}}*.txt")

    return wrapper
