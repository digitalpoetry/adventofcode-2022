from aoc.day08 import part1, part2

input_data = """30373
25512
65332
33549
35390
"""


def test_part1():
    assert part1(input_data) == 21


def test_part2():
    assert part2(input_data) == 8
