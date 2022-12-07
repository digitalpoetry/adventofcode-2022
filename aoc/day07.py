from typing import List, Optional, Dict

from aocd.models import Puzzle


class Directory:
    def __init__(self, name, *, parent: Optional['Directory']):
        self.name: str = name
        self.parent: Optional['Directory'] = parent
        self.children: Dict[str, 'Directory'] = {}
        self.leaves: Dict[str, int] = {}

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children.values()) + sum(self.leaves.values())

    def add_leaf(self, name: str, size: int) -> None:
        self.leaves[name] = size

    def add_dir(self, name: str) -> None:
        if name in self.children:
            return
        self.children[name] = Directory(name, parent=self)

    def cd(self, name: str) -> 'Directory':
        if name == "..":
            return self.parent or self
        return self.children[name]


def parse_filetree(input_data: str) -> Directory:
    root = Directory("/", parent=None)
    current_dir: Directory = root
    for line in input_data.splitlines()[1:]:
        token: List[str] = line.split()
        if line.startswith("$ ls"):
            continue
        elif line.startswith("$ cd"):
            current_dir = current_dir.cd(token[-1])
        elif line.startswith("dir"):
            current_dir.add_dir(token[-1])
        else:
            current_dir.add_leaf(token[1], int(token[0]))
    return root


def part1(input_data: str) -> int:
    result_sum = 0
    root = parse_filetree(input_data)
    walk = [root]
    while walk:
        current_dir = walk.pop()
        current_dir_size = current_dir.get_size()
        if current_dir_size < 100000:
            result_sum += current_dir_size
        for _, subdir in current_dir.children.items():
            walk.append(subdir)
    return result_sum


def part2(input_data: str) -> int:
    root = parse_filetree(input_data)
    filesystem_size = root.get_size()
    threshold = 40_000_000
    min_candidate = filesystem_size
    walk = [root]
    while walk:
        current_dir = walk.pop()
        current_dir_size = current_dir.get_size()
        if (filesystem_size - current_dir_size) < threshold \
                and current_dir_size < min_candidate:
            min_candidate = current_dir_size
        for _, subdir in current_dir.children.items():
            walk.append(subdir)
    return min_candidate


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=7)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
