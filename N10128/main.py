import sys
import collections


Q = collections.defaultdict(int)
Q[1, 1, 1] = 1
for n in range(2, 14):
    # Calculate by looking at the shortest
    # person since he cannot block anybody
    Q.update({
        (n, p, r): Q[n - 1, p - 1, r]  # Shortest first
        + Q[n - 1, p, r - 1]  # Shortest last
        + Q[n - 1, p, r] * (n - 2)  # Shortest in between
        for p in range(1, n + 1)
        for r in range(1, n + 1)})


def solve(n, p, r):
    return Q[n, p, r]


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        n, p, r = [int(x) for x in file.readline().split()]
        res.append('{}\n'.format(solve(n, p, r)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
