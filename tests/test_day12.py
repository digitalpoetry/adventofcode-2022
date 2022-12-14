from aoc.day12 import part1, part2

input_data = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def test_part1():
    assert part1(input_data) == 31


def test_part2():
    assert part2(input_data) == 29
