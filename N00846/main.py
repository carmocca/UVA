import sys
from math import floor
from math import sqrt


def solve(n):
    return floor(sqrt(n - 1) + sqrt(n + 1)) if n else 0


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        x, y = [int(x) for x in file.readline().split()]
        res.append('{}\n'.format(solve(y - x)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
