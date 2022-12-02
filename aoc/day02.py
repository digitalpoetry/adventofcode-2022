from enum import Enum

from aocd.models import Puzzle


class MatchResult(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6

    @staticmethod
    def from_str(s: str) -> 'MatchResult':
        match s:
            case 'X':
                return MatchResult.LOSE
            case 'Y':
                return MatchResult.DRAW
            case 'Z':
                return MatchResult.WIN


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @staticmethod
    def from_str(s: str) -> 'Shape':
        match s:
            case 'A' | 'X':
                return Shape.ROCK
            case 'B' | 'Y':
                return Shape.PAPER
            case 'C' | 'Z':
                return Shape.SCISSORS
            case _:
                raise ValueError(f"Invalid shape {s}")

    def play(self, s: 'Shape') -> int:
        match (self, s):
            case (Shape.ROCK, Shape.ROCK):
                result = MatchResult.DRAW
            case (Shape.ROCK, Shape.PAPER):
                result = MatchResult.WIN
            case (Shape.ROCK, Shape.SCISSORS):
                result = MatchResult.LOSE
            case (Shape.PAPER, Shape.ROCK):
                result = MatchResult.LOSE
            case (Shape.PAPER, Shape.PAPER):
                result = MatchResult.DRAW
            case (Shape.PAPER, Shape.SCISSORS):
                result = MatchResult.WIN
            case (Shape.SCISSORS, Shape.ROCK):
                result = MatchResult.WIN
            case (Shape.SCISSORS, Shape.PAPER):
                result = MatchResult.LOSE
            case (Shape.SCISSORS, Shape.SCISSORS):
                result = MatchResult.DRAW
            case _:
                raise NotImplementedError(f"No result implemented for play {self} {s}")
        return result.value + s.value


strategy = {
    (Shape.ROCK, MatchResult.WIN): Shape.PAPER,
    (Shape.ROCK, MatchResult.DRAW): Shape.ROCK,
    (Shape.ROCK, MatchResult.LOSE): Shape.SCISSORS,
    (Shape.PAPER, MatchResult.WIN): Shape.SCISSORS,
    (Shape.PAPER, MatchResult.DRAW): Shape.PAPER,
    (Shape.PAPER, MatchResult.LOSE): Shape.ROCK,
    (Shape.SCISSORS, MatchResult.WIN): Shape.ROCK,
    (Shape.SCISSORS, MatchResult.DRAW): Shape.SCISSORS,
    (Shape.SCISSORS, MatchResult.LOSE): Shape.PAPER,
}


def part1(input_data: str) -> int:
    matches = []
    for line in input_data.splitlines():
        matches.append((Shape.from_str(t) for t in line.split(' ')))
    return sum(a.play(b) for a, b in matches)


def part2(input_data: str) -> int:
    matches = []
    for line in input_data.splitlines():
        a, b = line.split()
        opponent_play = Shape.from_str(a)
        desired_result = MatchResult.from_str(b)
        strategy_play = strategy.get((opponent_play, desired_result))
        matches.append((opponent_play, strategy_play))
    return sum(a.play(b) for a, b in matches)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=2)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
