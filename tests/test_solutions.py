import pytest


@pytest.mark.parametrize(
    "day,part",
    [
        pytest.param(1, 1, id="1-1"),
        pytest.param(1, 2, id="1-2"),
        pytest.param(2, 1, id="2-1"),
    ],
)
def test_should_solve_puzzle(load_fixture, solve_puzzle, day: int, part: int) -> None:
    try:
        fixtures = load_fixture(day, part)
        for (input, expected) in fixtures:
            assert solve_puzzle(day, part, input) == expected
    except (FileNotFoundError, NotImplementedError) as e:
        pytest.skip(f"Reason: {e}")
