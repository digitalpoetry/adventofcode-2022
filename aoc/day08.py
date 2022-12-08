import math
from itertools import count
from typing import Dict, Generator, Tuple, Set

from aocd.models import Puzzle


def parse_heights(input_data: str) -> Tuple[int, int, Dict[Tuple[int, int], int]]:
    lines = input_data.splitlines()
    n_col = len(lines[0])
    n_row = len(lines)

    height: Dict[Tuple[int, int], int] = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            height[(row, col)] = int(char)

    return n_row, n_col, height


def part1(input_data: str) -> int:
    n_row, n_col, height = parse_heights(input_data)
    visible: Set[Tuple[int, int]] = set()

    # Look horizontally at the rows
    for row in range(n_row):
        max_height = -1
        for col in range(n_col):
            coord = (row, col)
            if height[coord] > max_height:
                max_height = height[coord]
                visible.add(coord)

        max_height = -1
        for col in reversed(range(n_col)):
            coord = (row, col)
            if height[coord] > max_height:
                max_height = height[coord]
                visible.add(coord)

    # Look veritically at the columns
    for col in range(n_col):
        max_height = -1
        for row in range(n_row):
            coord = (row, col)
            if height[coord] > max_height:
                max_height = height[coord]
                visible.add(coord)

        max_height = -1
        for row in reversed(range(n_row)):
            coord = (row, col)
            if height[coord] > max_height:
                max_height = height[coord]
                visible.add(coord)

    return len(visible)


def part2(input_data: str) -> int:
    n_row, n_col, height = parse_heights(input_data)
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    def view(coord: Tuple[int, int], direction: Tuple[int, int]) -> Generator[Tuple[int, int], None, None]:
        for multiplier in count(1):
            delta = [multiplier * d for d in direction]
            yield coord[0] + delta[0], coord[1] + delta[1]

    top_scenic_score = 0
    for row in range(1, n_row - 1):
        for col in range(1, n_col - 1):
            coord = (row, col)
            current_tree_height = height[coord]
            scenic = []
            for direction in directions:
                c = 0
                for tree in view((row, col), direction):
                    if tree not in height:
                        break
                    c += 1
                    if height[tree] >= current_tree_height:
                        break
                scenic.append(c)
            scenic_score = math.prod(scenic)
            if scenic_score > top_scenic_score:
                top_scenic_score = scenic_score

    return top_scenic_score


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=8)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
