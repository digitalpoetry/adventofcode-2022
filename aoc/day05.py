from io import StringIO
from typing import List

from aocd.models import Puzzle


def read_blocks(s: str, n_characters: int) -> List[str]:
    result: List[str] = []
    sio = StringIO(s)
    while chunk := sio.read(n_characters):
        result.append(chunk)
    return result


def parse_stacks(stacks_input: str) -> List[List[str]]:
    stacks: List[List[str]] = []
    for line in reversed(stacks_input.splitlines()[:-1]):
        crates = [block.strip("[] ") for block in read_blocks(line, 4)]
        if not stacks:
            stacks = [list() for _ in crates]
        for s, c in zip(stacks, crates):
            s.append(c) if c else None
    return stacks


def part1(input_data: str) -> str:
    stacks_input, moves_input = input_data.split('\n\n')
    stacks = parse_stacks(stacks_input)
    for line in moves_input.splitlines():
        _, a, _, b, _, c = line.split()
        count, from_stack, to_stack = int(a), int(b) - 1, int(c) - 1
        for i in range(count):
            crate = stacks[from_stack].pop()
            stacks[to_stack].append(crate)
    return ''.join(stack[-1] for stack in stacks)


def part2(input_data: str) -> str:
    stacks_input, moves_input = input_data.split('\n\n')
    stacks = parse_stacks(stacks_input)
    for line in moves_input.splitlines():
        _, a, _, b, _, c = line.split()
        count, from_stack, to_stack = int(a), int(b) - 1, int(c) - 1
        buffer: List[str] = []
        for i in range(count):
            crate = stacks[from_stack].pop()
            buffer.append(crate)
        for crate in reversed(buffer):
            stacks[to_stack].append(crate)
    return ''.join(stack[-1] for stack in stacks)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=5)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
