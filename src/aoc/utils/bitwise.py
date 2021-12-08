from typing import List
from typing import Union


def common_bits(bits: List[int]) -> Union[int, int]:
    bitset = set(bits)
    return min(bitset, key=bits.count), max(bitset, key=bits.count)
