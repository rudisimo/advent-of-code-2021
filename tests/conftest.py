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
            solver = getattr(importlib.import_module(f"aoc.day_{day:0{2}}"), f"solution_{part}")
        except (AttributeError, ModuleNotFoundError) as e:
            raise NotImplementedError(e)
        else:
            return str(solver(input))

    return wrapper


@pytest.fixture
def load_fixtures():
    def wrapper(day: int, part: int, patterns: List[str]) -> Tuple[List[str], Optional[str]]:
        for fixture_name in patterns:
            fixture_glob = f"{Path().absolute()}/tests/fixtures/{day:0{2}}-{fixture_name}.txt"
            fixture_files = glob(fixture_glob)
            for fixture in fixture_files:
                try:
                    with open(fixture) as fp:
                        samples = fp.read().split("--EXPECT--\n")
                        yield (samples[0].splitlines(), samples[part].strip())
                except (IndexError):
                    yield ([], None)
            if not fixture_files:
                raise FileNotFoundError(f"fixture(s) not found: {fixture_glob}")

    return wrapper
