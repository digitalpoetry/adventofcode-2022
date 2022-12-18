import re
from dataclasses import dataclass
from typing import List, Optional, Tuple

from aocd.models import Puzzle


@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int
    is_end_of_interval: bool = False


@dataclass(order=True)
class Interval:
    start: int
    end: int  # inclusive

    def range(self) -> int:
        return (self.end - self.start) + 1


pattern = re.compile(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)')


def part1(input_data: str, *, row: int) -> int:
    scanners, beacons = parse_sensors_beacons(input_data)
    coverage = get_coverage(scanners, beacons, row=row)

    beacons_on_row = sum(1 for b in set(beacons) if b.y == row)
    return sum(interval.range() for interval in coverage) - beacons_on_row


def parse_sensors_beacons(input_data: str) -> Tuple[List[Point], List[Point]]:
    scanners, beacons = [], []
    for line in input_data.splitlines():
        match = pattern.search(line)
        assert match is not None
        sx, sy, bx, by = (int(n) for n in match.groups())
        scanner, beacon = Point(sx, sy), Point(bx, by)
        scanners.append(scanner)
        beacons.append(beacon)
    return scanners, beacons


def get_coverage(scanners, beacons, *, row: int) -> List[Interval]:
    intervals: List[Interval] = []
    for scanner, beacon in zip(scanners, beacons):
        dist = manhattan_distance(scanner, beacon)
        vertical = abs(row - scanner.y)
        if vertical <= dist:
            horizontal = dist - vertical
            intervals.append(Interval(scanner.x - horizontal, scanner.x + horizontal))

    events: List[Point] = []
    for interval in intervals:
        events.append(Point(interval.start, row, is_end_of_interval=False))
        events.append(Point(interval.end, row, is_end_of_interval=True))
    events.sort()

    open_intervals = 0
    current_start: Optional[int] = None
    coverage: List[Interval] = []
    for point in events:
        if not point.is_end_of_interval:
            if open_intervals == 0:
                assert current_start is None
                current_start = point.x
            open_intervals += 1
        else:
            open_intervals -= 1
            if open_intervals == 0:
                assert current_start is not None
                coverage.append(Interval(current_start, point.x))
                current_start = None

    assert open_intervals == 0
    return coverage


def manhattan_distance(p1, p2) -> int:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def part2(input_data: str, *, limit_search: int) -> int:
    scanners, beacons = parse_sensors_beacons(input_data)
    for y in range(limit_search + 1):
        coverage = [
            interval for interval in get_coverage(scanners, beacons, row=y)
            if not (interval.end < 0 or interval.start > limit_search)
        ]
        if len(coverage) > 1:
            return (coverage[0].end + 1) * 4_000_000 + y
    return 0


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=15)
    print(part1(puzzle.input_data, row=2_000_000))
    print(part2(puzzle.input_data, limit_search=4_000_000))
