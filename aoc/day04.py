from dataclasses import dataclass
from typing import List, Tuple, Any

from aocd.models import Puzzle


@dataclass(order=True)
class Interval:
    start: int
    end: int  # exclusive

    def __contains__(self, item: Any) -> bool:
        if type(item) != Interval:
            raise NotImplementedError
        return self.start <= item.start and self.end >= item.end

    def overlaps(self, other: 'Interval') -> bool:
        return min(self.end, other.end) > max(self.start, other.start)


def parse(input_data: str) -> List[Tuple[Interval, Interval]]:
    pairs = []
    for line in input_data.splitlines():
        a, b, c, d = [int(token) for token in line.replace('-', ',').split(',')]
        pairs.append((Interval(a, b + 1), Interval(c, d + 1)))
    return pairs


def part1(input_data: str) -> int:
    pairs = parse(input_data)
    count = 0
    for first, second in pairs:
        if first in second or second in first:
            count += 1
    return count


def part2(input_data: str) -> int:
    pairs = parse(input_data)
    count = 0
    for first, second in pairs:
        if first.overlaps(second):
            count += 1
    return count


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=4)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
