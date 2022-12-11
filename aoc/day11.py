import math
import re
from collections import deque
from typing import Sequence, List, Optional, Tuple, Callable, Any

from aocd.models import Puzzle


class Monkey:
    def __init__(self,
                 monkey_id: int,
                 items: Sequence[int],
                 op: Callable[[Any], int],
                 op_values: Tuple[Optional[int], Optional[int]],
                 divisor: int,
                 true_monkey: int,
                 false_monkey: int
                 ):
        self.monkey_id = monkey_id
        self.items = deque(items)
        self.op = op
        self.op_values = op_values
        self.n_inspections = 0
        self.divisor = divisor
        self.false_monkey = false_monkey
        self.true_monkey = true_monkey

    def throw_item(self, worry_reduction_function) -> (int, int):
        assert self.items, "this monkey has no items to throw"
        self.n_inspections += 1
        worry_level = self.items.popleft()
        worry_level = self.op(v if v else worry_level for v in self.op_values)
        worry_level = worry_reduction_function(worry_level)
        return self.test(worry_level), worry_level

    def test(self, worry_level: int) -> int:
        return self.true_monkey if worry_level % self.divisor == 0 else self.false_monkey


def int_or_none(s: str) -> Optional[int]:
    try:
        return int(s)
    except ValueError:
        return None


def parse_monkey(section: str) -> Monkey:
    lines = section.splitlines()
    matches = {
        'monkey_id': re.search(r'Monkey (\d+):', lines[0]),
        'items': re.search(r'Starting items: (.*)', lines[1]),
        'operator': re.search(r'Operation: new = (.*)', lines[2]),
        'divisor': re.search(r'Test: divisible by (\d+)', lines[3]),
        'true_monkey': re.search(r'If true: throw to monkey (\d+)', lines[4]),
        'false_monkey': re.search(r'If false: throw to monkey (\d+)', lines[5]),
    }
    if all(matches.values()):
        monkey_id = int(matches['monkey_id'].group(1))
        items = [int(i) for i in matches['items'].group(1).split(", ")]
        a, operator, b = matches['operator'].group(1).split()
        assert operator in ('+', '*')
        op = sum if operator == '+' else math.prod
        op_values = int_or_none(a), int_or_none(b)
        divisor = int(matches['divisor'].group(1))
        true_monkey = int(matches['true_monkey'].group(1))
        false_monkey = int(matches['false_monkey'].group(1))
    else:
        raise ValueError
    return Monkey(monkey_id, items, op, op_values, divisor, true_monkey, false_monkey)


def part1(input_data: str, n_rounds: int = 20) -> int:
    monkeys: List[Monkey] = []
    for section in input_data.split("\n\n"):
        monkey = parse_monkey(section)
        monkeys.append(monkey)

    def worry_reduction_function(worry_level: int):
        return worry_level // 3

    for _ in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                to_monkey, item = monkey.throw_item(worry_reduction_function)
                monkeys[to_monkey].items.append(item)

    top_2 = sorted(m.n_inspections for m in monkeys)[-2:]
    return math.prod(top_2)


def part2(input_data: str, n_rounds: int = 10_000) -> int:
    monkeys: List[Monkey] = []
    for section in input_data.split("\n\n"):
        monkey = parse_monkey(section)
        monkeys.append(monkey)

    lcm = math.prod(m.divisor for m in monkeys)

    def worry_reduction_function(worry_level: int):
        return worry_level % lcm

    for _ in range(n_rounds):
        for monkey in monkeys:
            while monkey.items:
                to_monkey, item = monkey.throw_item(worry_reduction_function)
                monkeys[to_monkey].items.append(item)

    top_2 = sorted(m.n_inspections for m in monkeys)[-2:]
    return math.prod(top_2)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=11)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
