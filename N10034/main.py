import sys
import os
import math
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

from lib.graphs import UndirectedGraph
from lib.graphs import minimum_spanning_tree


def euclidean_distance(p1, p2):
    return math.sqrt(sum([(x - y) ** 2 for x, y in zip(p1, p2)]))


def solve(freckles):
    n = len(freckles)
    graph = UndirectedGraph()

    for i in range(n):
        graph.new_node(i)

    for i in range(n):
        for j in range(i, n):
            graph.new_edge(i, j, cost=euclidean_distance(
                freckles[i], freckles[j]))

    mst = minimum_spanning_tree(graph)
    return sum(graph.get_edge(e_id)['cost'] for e_id in mst)


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        file.readline()
        n = int(file.readline())
        freckles = [tuple(float(x)
                          for x in file.readline().split())
                    for _ in range(n)]
        res.append('{:0.2f}\n'.format(solve(freckles)))
        res.append('\n')
    return res[:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
