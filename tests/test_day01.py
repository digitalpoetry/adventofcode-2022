from aoc.day01 import part1, part2

input_data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_part1():
    assert part1(input_data) == 24000


def test_part2():
    assert part2(input_data) == 45000
