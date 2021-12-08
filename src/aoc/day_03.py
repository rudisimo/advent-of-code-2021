from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from typing import List

from aoc.utils import common_bits


@dataclass
class Condition:
    bits: List[int] = field(default_factory=list)

    @property
    def decimal(self) -> int:
        return int("".join(list(map(str, self.bits))), 2)

    @staticmethod
    def from_string(value: str) -> Condition:
        bits = list(map(int, list(value)))
        return Condition(bits=bits)

    def __getitem__(self, key: int) -> int:
        return self.bits[key]

    def __setitem__(self, key: int, value: int) -> None:
        self.bits.insert(key, value)

    def __len__(self) -> int:
        return len(self.bits)

    def __mul__(self, other: Condition) -> int:
        return self.decimal * other.decimal

    def __rmul__(self, other: Condition) -> int:
        return other.decimal * self.decimal

    def __copy__(self) -> Condition:
        return Condition(self.bits)


def answer_1(input: List[str]) -> int:
    gamma_rate = Condition()
    epsilon_rate = Condition()

    normalized_list = list(map(Condition.from_string, input))
    for n in range(len(normalized_list[0])):
        lcb, mcb = common_bits([c[n] for c in normalized_list])
        gamma_rate[n] = mcb
        epsilon_rate[n] = lcb

    power_consumption = gamma_rate * epsilon_rate

    return power_consumption


def answer_2(input: List[str]) -> int:
    o2_scrubber_rating = Condition()
    co2_scrubber_rating = Condition()

    normalized_list = list(map(Condition.from_string, input))
    normalized_bits = len(normalized_list[0])

    o2_scrubber_list = normalized_list.copy()
    for n in range(normalized_bits):
        lcb, mcb = common_bits([c[n] for c in o2_scrubber_list])
        o2_scrubber_list = list(
            [c for c in o2_scrubber_list if (lcb != mcb and c[n] == mcb) or (lcb == mcb and c[n] == 1)]
        )
        if len(o2_scrubber_list) == 1:
            o2_scrubber_rating = o2_scrubber_list.pop()
            break

    co2_scrubber_list = normalized_list.copy()
    for n in range(normalized_bits):
        lcb, mcb = common_bits([c[n] for c in co2_scrubber_list])
        co2_scrubber_list = list(
            [c for c in co2_scrubber_list if (lcb != mcb and c[n] == lcb) or (lcb == mcb and c[n] == 0)]
        )
        if len(co2_scrubber_list) == 1:
            co2_scrubber_rating = co2_scrubber_list.pop()
            break

    life_support_rating = o2_scrubber_rating * co2_scrubber_rating

    return life_support_rating
