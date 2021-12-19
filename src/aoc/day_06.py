from typing import List


def evolve(school: List[int], days: int) -> int:
    school_phases = [0] * 9
    for age in school:
        school_phases[age] += 1

    for _ in range(days):
        newborn_fish = 0
        for phase in range(9):
            if phase == 0:
                newborn_fish = school_phases[0]
                school_phases[0] = 0
            else:
                school_phases[phase - 1] = school_phases[phase]
        school_phases[8] = newborn_fish
        school_phases[6] += newborn_fish

    return sum(school_phases)


def solution_1(input: List[str]) -> int:
    normalized_list = [int(d) for d in input.pop(0).split(",")]
    result = evolve(normalized_list, 80)

    return result


def solution_2(input: List[str]) -> int:
    normalized_list = [int(d) for d in input.pop(0).split(",")]
    result = evolve(normalized_list, 256)

    return result
