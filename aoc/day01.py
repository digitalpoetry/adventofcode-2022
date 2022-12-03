from typing import List

from aocd.models import Puzzle


def parse(lines: str) -> List[int]:
    sections = lines.split('\n\n')
    calories_carried = []
    for section in sections:
        c = sum(int(line) for line in section.splitlines())
        calories_carried.append(c)
    return calories_carried


def part1(input_data: str) -> int:
    calories_carried = parse(input_data)
    return max(calories_carried)


def part2(input_data: str) -> int:
    calories_carried = parse(input_data)
    return sum(sorted(calories_carried)[-3:])


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
