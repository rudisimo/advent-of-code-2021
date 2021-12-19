from typing import List

import pytest


@pytest.mark.parametrize(
    "day,part,fixtures",
    [
        pytest.param(1, 1, ["example", "input"], id="1-1"),
        pytest.param(1, 2, ["example", "input"], id="1-2"),
        pytest.param(2, 1, ["example", "input"], id="2-1"),
        pytest.param(2, 2, ["example", "input"], id="2-2"),
        pytest.param(3, 1, ["example", "input"], id="3-1"),
        pytest.param(3, 2, ["example", "input"], id="3-2"),
        pytest.param(4, 1, ["example", "input"], id="4-1"),
        pytest.param(4, 2, ["example", "input"], id="4-2"),
        pytest.param(5, 1, ["example", "input"], id="5-1"),
        pytest.param(5, 2, ["example", "input"], id="5-2"),
    ],
)
def test_should_solve_puzzle(load_fixtures, solve_puzzle, day: int, part: int, fixtures: List[str]) -> None:
    try:
        fixtures = load_fixtures(day, part, fixtures)
        for (input, expected) in fixtures:
            assert solve_puzzle(day, part, input) == expected
    except (FileNotFoundError, NotImplementedError) as e:
        pytest.skip(f"Reason: [{type(e).__name__}] {e}")
