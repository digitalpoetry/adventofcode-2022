import copy
import itertools

from aocd.models import Puzzle


def nwise(iterable, n: int):
    # Make n tees at successive positions along the iterable.
    tees = list(itertools.tee(iterable, 1))
    for _ in range(n - 1):
        tees.append(copy.copy(tees[-1]))
        next(tees[-1])
    return zip(*tees)


def part1(input_data: str) -> int:
    for i, quadtruple in enumerate(nwise(input_data, 4), 4):
        if len(set(quadtruple)) == len(quadtruple):
            return i
    raise ValueError


def part2(input_data: str) -> int:
    for i, tup in enumerate(nwise(input_data, 14), 14):
        if len(set(tup)) == len(tup):
            return i
    raise ValueError


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=6)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
