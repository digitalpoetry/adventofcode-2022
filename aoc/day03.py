from string import ascii_lowercase, ascii_uppercase
from typing import Tuple, Dict

from aocd.models import Puzzle

priority: Dict[str, int] = dict(
    (letter, i)
    for i, letter in enumerate(ascii_lowercase + ascii_uppercase, start=1))


def halve_str(s: str) -> Tuple[str, str]:
    assert len(s) % 2 == 0, "String of even length is expected"
    median = len(s) // 2
    return s[:median], s[median:]


def triplets(iterable):
    """
    Return elements as triplets from an iterable.
    triplets('ABCDEFGHI') -> ABC DEF GHI
    """
    a = iter(iterable)
    return zip(a, a, a)


def score_duplicate(*components: str) -> int:
    sets = [set(s) for s in components]
    intersection = set.intersection(*sets)
    assert len(
        intersection) == 1, "Only one duplicate within components is expected"
    return priority[intersection.pop()]


def part1(input_data: str) -> int:
    return sum(
        score_duplicate(*halve_str(line)) for line in input_data.splitlines())


def part2(input_data: str) -> int:
    return sum(
        score_duplicate(*elf_group)
        for elf_group in triplets(input_data.splitlines()))


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=3)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
