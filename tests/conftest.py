from glob import glob
from pathlib import Path
from typing import List
from typing import Optional
from typing import Tuple

import pytest


@pytest.fixture
def load_fixture():
    def _wrapper(day: int, part: int) -> Tuple[List[str], Optional[str]]:
        fixtures = glob(f"{Path().absolute()}/tests/fixtures/{day:0{2}}*.txt")
        for fixture in fixtures:
            try:
                with open(fixture) as f:
                    samples = f.read().split("---------------------\n")
                    yield (samples[0].splitlines(), samples[part].strip())
            except (IndexError):
                yield ([], None)
        else:
            raise FileNotFoundError(f"no fixtures: tests/fixtures/{day:0{2}}*.txt")

    return _wrapper
