from aoc.day04 import part1, part2, Interval

input_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_part1():
    assert part1(input_data) == 2


def test_part2():
    assert part2(input_data) == 4


def test_interval_contains():
    assert Interval(2, 2) in Interval(2, 2)
    assert Interval(2, 2) in Interval(2, 6)
    assert Interval(2, 2) in Interval(1, 2)

    assert Interval(2, 3) in Interval(0, 3)
    assert Interval(2, 3) in Interval(2, 7)
    assert Interval(2, 3) in Interval(0, 10)

    assert Interval(2, 5) not in Interval(0, 2)
    assert Interval(2, 5) not in Interval(2, 3)
    assert Interval(2, 5) not in Interval(3, 7)
    assert Interval(2, 5) not in Interval(0, 3)


def test_interval_overlaps():
    assert Interval(3, 5).overlaps(Interval(3, 5))
    assert Interval(3, 5).overlaps(Interval(4, 6))
    assert Interval(3, 5).overlaps(Interval(2, 4))
    assert Interval(3, 5).overlaps(Interval(1, 9))

    assert not Interval(3, 5).overlaps(Interval(5, 6))
    assert not Interval(3, 5).overlaps(Interval(7, 9))
