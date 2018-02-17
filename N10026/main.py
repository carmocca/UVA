import sys
import collections

Order = collections.namedtuple('Order', ['time', 'penalty'])


def solve(orders):
    return [idx
            for idx, order in sorted(
                [(idx + 1, order) for idx, order in enumerate(orders)],
                key=lambda order: order[1].time / order[1].penalty)]


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        n = int(file.readline())
        orders = [Order(*map(int, file.readline().split())) for _ in range(n)]
        res.append(' '.join(map(str, solve(orders))) + '\n')
        res.append('\n')
        file.readline()
    return res[:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
