from aoc.day03 import part1, part2, triplets, halve_str

input_data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_part1():
    assert part1(input_data) == 157


def test_part2():
    assert part2(input_data) == 70


def test_halve_str():
    assert halve_str("ABCDEF") == ("ABC", "DEF")


def test_triplets():
    assert list(triplets("ABCDEFGHI")) == [("A", "B", "C"), ("D", "E", "F"),
                                           ("G", "H", "I")]
