from aoc.day09 import part1, part2

input_data1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

input_data2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def test_part1():
    assert part1(input_data1) == 13


def test_part2():
    assert part2(input_data1) == 1
    assert part2(input_data2) == 36
