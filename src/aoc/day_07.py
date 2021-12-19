from typing import List


def distance(positions: List[int], position: int, exponential_rate: bool = True) -> int:
    distance = 0
    for step, crab_position in enumerate(positions, 1):
        # calculate absolute difference
        if crab_position < position:
            diff = abs(position - crab_position)
        else:
            diff = abs(crab_position - position)

        # use proper rate formula
        if exponential_rate is True:
            distance += int(diff * (diff + 1) / 2)
        else:
            distance += diff

    return distance


def solution_1(input: List[str]) -> int:
    normalized_list = sorted([int(d) for d in input.pop(0).split(",")])
    fuel_costs = [distance(normalized_list, n, False) for n in range(normalized_list[0], normalized_list[-1])]
    result = min(fuel_costs)

    return result


def solution_2(input: List[str]) -> int:
    normalized_list = sorted([int(d) for d in input.pop(0).split(",")])
    fuel_costs = [distance(normalized_list, n, True) for n in range(normalized_list[0], normalized_list[-1])]
    result = min(fuel_costs)

    return result
