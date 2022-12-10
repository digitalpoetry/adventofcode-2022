import itertools
from collections import deque
from enum import Enum
from typing import Sequence, Generator

from aocd.models import Puzzle


class Command(Enum):
    noop = (1, lambda reg, *args: reg)
    addx = (2, lambda reg, *args: reg + int(args[0]))

    def get_wait_cycles(self) -> int:
        return self.value[0]

    def execute(self, register: int, *args: str) -> int:
        return self.value[1](register, *args)


class Instruction:
    def __init__(self, raw: str):
        command, *args = raw.split()
        self.command = Command[command]
        self.args = args

    def get_wait_cycles(self):
        return self.command.get_wait_cycles()

    def apply(self, register: int) -> int:
        return self.command.execute(register, *self.args)


def chunks(sequence: Sequence, n: int) -> Generator[Sequence, None, None]:
    """Yield successive n-sized chunks from a sequence."""
    for i in range(0, len(sequence), n):
        yield sequence[i:i + n]


def part1(input_data: str) -> int:
    register = 1
    tape = deque(input_data.splitlines())
    current_instruction = Instruction(tape.popleft())
    busy = current_instruction.get_wait_cycles()

    result = []
    for cycle in itertools.count(1):
        if cycle in (20, 60, 100, 140, 180, 220):
            result.append((cycle, register))

        busy = busy - 1
        if busy:
            continue
        register = current_instruction.apply(register)
        if not tape:
            break
        current_instruction = Instruction(tape.popleft())
        busy = current_instruction.get_wait_cycles()

    return sum(cycle * register for cycle, register in result)


def part2(input_data: str) -> int:
    register = 1
    tape = deque(input_data.splitlines())
    current_instruction = Instruction(tape.popleft())
    busy = current_instruction.get_wait_cycles()

    result = []
    for crt_head in itertools.count():
        sprite_positions = (register - 1, register, register + 1)
        if crt_head % 40 in sprite_positions:
            result.append("#")
        else:
            result.append(".")

        busy = busy - 1
        if busy:
            continue
        register = current_instruction.apply(register)
        if not tape:
            break
        current_instruction = Instruction(tape.popleft())
        busy = current_instruction.get_wait_cycles()

    for crt_row in chunks(result, 40):
        print(''.join(crt_row))
    return 0

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=10)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
