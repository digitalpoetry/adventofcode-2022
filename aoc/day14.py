import copy
from itertools import count, tee
from math import copysign
from typing import List, Set, Tuple

from aocd.models import Puzzle

Pair = Tuple[int, int]


def nwise(iterable, n: int):
    """
    Make n tees at successive positions along the iterable.
    nwise("ABCDE", 3) -> ABC BCD CDE
    """
    tees = list(tee(iterable, 1))
    for _ in range(n - 1):
        tees.append(copy.copy(tees[-1]))
        next(tees[-1])
    return zip(*tees)


def line_to_pairs(line: str) -> List[Tuple[int, int]]:
    pairs = []
    for point in line.split(' -> '):
        a, b = point.split(',')
        pairs.append((int(a), int(b)))
    return pairs


def sign(value: int) -> int:
    if value == 0:
        return 0
    return int(copysign(1, value))


def map_world(input_data: str) -> Set[Pair]:
    world = set()
    for line in input_data.splitlines():
        pairs = line_to_pairs(line)
        for (x1, y1), (x2, y2) in nwise(pairs, 2):
            if dx := sign(x2 - x1):
                for x in range(x1, x2 + dx, dx):
                    world.add((x, y1))
            elif dy := sign(y2 - y1):
                for y in range(y1, y2 + dy, dy):
                    world.add((x1, y))
    return world


def drop_sand(world, floor_height: int, start=(500, 0)) -> bool:
    """Returns true if end condition is reached."""
    x, y = start
    while True:
        if y == floor_height:
            return True

        if (down := (x, y + 1)) not in world:
            x, y = down
        elif (down_left := (x - 1, y + 1)) not in world:
            x, y = down_left
        elif (down_right := (x + 1, y + 1)) not in world:
            x, y = down_right
        else:
            if (x, y) in world:
                return True
            world.add((x, y))
            return False


def part1(input_data: str) -> int:
    world = map_world(input_data)
    floor_height = max(y for (_, y) in world) + 2
    for i in count():
        if drop_sand(world, floor_height):
            return i
    raise Exception("unreachable")



def part2(input_data: str) -> int:
    world = map_world(input_data)
    floor_height = max(y for (_, y) in world) + 2
    for x in range(-1000, 1000):
        world.add((x, floor_height))
    for i in count():
        if drop_sand(world, floor_height):
            return i
    raise Exception("unreachable")


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=14)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
