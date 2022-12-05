from aoc.day05 import part1, part2, read_blocks

input_data = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def test_part1():
    assert part1(input_data) == "CMZ"


def test_part2():
    assert part2(input_data) == "MCD"


def test_read_block():
    assert read_blocks("abcde", 2) == ["ab", "cd", "e"]
