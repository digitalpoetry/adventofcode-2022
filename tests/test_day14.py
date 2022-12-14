from aoc.day14 import part1, part2

input_data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""


def test_part1():
    assert part1(input_data) == 24


def test_part2():
    assert part2(input_data) == 93
