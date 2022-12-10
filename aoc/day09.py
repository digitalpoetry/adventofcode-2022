import copy
import itertools
from dataclasses import dataclass
from typing import Iterable

from aocd.models import Puzzle


def nwise(iterable, n: int):
    """
    Make n tees at successive positions along the iterable.
    nwise("ABCDE", 3) -> ABC BCD CDE
    """
    tees = list(itertools.tee(iterable, 1))
    for _ in range(n - 1):
        tees.append(copy.copy(tees[-1]))
        next(tees[-1])
    return zip(*tees)


@dataclass(frozen=True)
class Coord:
    x: int = 0
    y: int = 0

    def is_touching(self, other: 'Coord') -> bool:
        for i, j in itertools.product((-1, 0, 1), repeat=2):
            if other == Coord(self.x + i, self.y + j):
                return True
        return False

    def nearest_touching(self) -> Iterable['Coord']:
        return [
            self.move('U'),
            self.move('D'),
            self.move('L'),
            self.move('R'),
            self.move('U').move('L'),
            self.move('U').move('R'),
            self.move('D').move('L'),
            self.move('D').move('R'),
        ]

    def move(self, direction: str):
        match direction:
            case 'U':
                return Coord(self.x, self.y + 1)
            case 'D':
                return Coord(self.x, self.y - 1)
            case 'L':
                return Coord(self.x - 1, self.y)
            case 'R':
                return Coord(self.x + 1, self.y)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def part1(input_data: str) -> int:
    head = Coord()
    tail = Coord()
    visited = {tail}
    for line in input_data.splitlines():
        d, steps = line.split()
        for _ in range(int(steps)):
            head = head.move(d)
            if not tail.is_touching(head):
                tail = [t for t in head.nearest_touching() if tail.is_touching(t)][0]
                visited.add(tail)
    return len(visited)


def part2(input_data: str) -> int:
    rope = [Coord() for _ in range(10)]
    visited = {rope[-1]}
    for line in input_data.splitlines():
        d, steps = line.split()
        for _ in range(int(steps)):
            new_rope = [rope[0].move(d)]
            for i in range(1, len(rope)):
                head = new_rope[-1]
                tail = rope[i]
                if not tail.is_touching(head):
                    tail = [t for t in head.nearest_touching() if tail.is_touching(t)][0]
                new_rope.append(tail)
            rope = new_rope
            visited.add(rope[-1])
    return len(visited)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=9)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
