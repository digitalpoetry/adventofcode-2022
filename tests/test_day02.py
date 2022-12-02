from aoc.day02 import part1, part2

input_data = """A Y
B X
C Z
"""


def test_part1():
    assert part1(input_data) == 15


def test_part2():
    assert part2(input_data) == 12
