import collections
import sys

Elephant = collections.namedtuple('Elephant', ['id', 'weight', 'iq'])


def is_feasible(elephant1, elephant2):
    return (elephant1.weight < elephant2.weight
            and elephant1.iq > elephant2.iq)


def recover_path(pred, pos):
    if pos >= 0:
        recover_path(pred, pred[pos])
    yield pos


def solve(elephants):
    n = len(elephants)
    by_weight = sorted(elephants, key=lambda e: e.weight)
    l = [1] * n
    pred = [-1] * n

    # Calculate solution and predecessors
    for i in range(n):
        e1 = elephants[i]
        for j in range(i + 1, n):
            e2 = elephants[j]
            if is_feasible(e1, e2):
                if l[i] + 1 > l[j]:
                    l[j] = l[i] + 1
                    pred[j] = i
    print(l)
    print(pred)

    # Return the path using the predecessors
    pos = n - 1
    for i in range(pos-1, -1, -1):
        if l[i] > l[pos]:
            pos = i
    # pos now has the maximum's position
    print('pos', pos)

    path = recover_path(pred, pos)
    return [by_weight[pos].id for pos in path]


def main(file):
    elephants = [Elephant(i + 1, *(int(x) for x in line.split()))
                 for i, line in enumerate(file)]
    return solve(elephants)


if __name__ == '__main__':
    sequence = main(sys.stdin)
    print(len(sequence))
    for elephant in sequence:
        print(elephant)
