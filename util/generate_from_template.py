from pathlib import Path

import click


@click.command()
@click.option('--day', required=True, type=int)
def generate(day: int):
    src_path = Path(f'aoc/day{day:02}.py')
    test_path = Path(f'tests/test_day{day:02}.py')

    if src_path.exists():
        raise ValueError(f"{src_path} already exists")
    if test_path.exists():
        raise ValueError(f"{test_path} already exists")

    src_path.write_text(f'''from aocd.models import Puzzle


def part1(input_data: str) -> int:
    return 0


def part2(input_data: str) -> int:
    return 0


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day={day})
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
''')

    test_path.write_text(f'''from aoc.day{day} import part1, part2

input_data = """
"""


def test_part1():
    assert part1(input_data) == 0


def test_part2():
    assert part2(input_data) == 0
''')


if __name__ == '__main__':
    generate()
