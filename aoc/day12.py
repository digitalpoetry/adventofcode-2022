import re
import networkx as nx
from string import ascii_lowercase
from typing import List, Tuple
import matplotlib.pyplot as plt

from aocd.models import Puzzle
from networkx import DiGraph


def parse_graph(block: str) -> Tuple[DiGraph, int, int]:
    height = len(block.splitlines())
    width = len(block.splitlines()[0])

    def parse_height(symbol: str) -> int:
        if symbol == 'S':
            symbol = 'a'
        if symbol == 'E':
            symbol = 'z'
        return ascii_lowercase.index(symbol)

    def get_neighbours(node: int) -> List[int]:
        row, col = divmod(node, width)
        neighbours = filter(lambda t: 0 <= t[0] < height and 0 <= t[1] < width,
                            [
                                (row, col - 1),
                                (row + 1, col),
                                (row - 1, col),
                                (row, col + 1),
                            ])
        return list(t[0] * width + t[1] for t in neighbours)

    nodes: str = re.sub(r'\s+', '', block)
    start_index = nodes.index('S')
    end_index = nodes.index('E')

    g = DiGraph()
    for i, symbol in enumerate(nodes):
        g.add_node(i, height=parse_height(symbol))

    for i in range(len(nodes)):
        for n in get_neighbours(i):
            if g.nodes[n]['height'] <= g.nodes[i]['height'] + 1:
                g.add_edge(i, n)

    return g, start_index, end_index


def part1(input_data: str) -> int:
    g, start_index, end_index = parse_graph(input_data)
    return len(nx.dijkstra_path(g, start_index, end_index)) - 1


def part2(input_data: str) -> int:
    g, start_index, end_index = parse_graph(input_data)
    candidate_start = [n for n in g.nodes if g.nodes[n]['height'] == 0]
    shortest_path = len(g.nodes)
    for start in candidate_start:
        try:
            path_length = len(nx.dijkstra_path(g, start, end_index)) - 1
            if shortest_path > path_length:
                shortest_path = path_length
        except nx.NetworkXNoPath:
            pass
    return shortest_path


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=12)
    print(part1(puzzle.input_data))
    print(part2(puzzle.input_data))
