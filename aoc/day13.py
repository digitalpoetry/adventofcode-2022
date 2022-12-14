from functools import cmp_to_key
from typing import Union, List

from aocd.models import Puzzle

Value = Union[List['Value'], int]


def parse(*lines: str) -> List[Value]:
    return [eval(line) for line in lines]


def cmp(left: Value, right: Value) -> int:
    if isinstance(left, list) and isinstance(right, list):
        for a, b in zip(left, right):
            if (diff := cmp(a, b)) != 0:
                return diff
        return cmp(len(left), len(right))
    elif isinstance(left, list):
        return cmp(left, [right])
    elif isinstance(right, list):
        return cmp([left], right)
    else:
        return (left > right) - (left < right)


def part1(input_data: str) -> int:
    blocks = input_data.split("\n\n")
    ordered_indices = []
    for i, block in enumerate(blocks, start=1):
        left, right = parse(*block.split())
        if cmp(left, right) <= 0:
            ordered_indices.append(i)
    return sum(ordered_indices)


def part2(input_data: str) -> int:
    lines = [line for line in input_data.split() if line]
    packets: List[Value] = [parse(p) for p in lines]
    packets += [0, [[2]], [[6]]]
    packets.sort(key=cmp_to_key(cmp))
    return packets.index([[2]]) * packets.index([[6]])


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=13)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
