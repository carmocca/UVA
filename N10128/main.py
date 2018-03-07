import sys
from math import factorial

factorials = {n: factorial(n) for n in range(13)}


def combination(n, k):
    return int((factorials[n]) / ((factorials[k]) * factorials[n - k]))


combinations = {(n, k): combination(n, k)
                for n in range(13) for k in range(n + 1)}
import pprint
# pprint.pprint(factorials)
# pprint.pprint(combinations)

Q = {(n, n, 1): 1 for n in range(13)}
#Q.update({(i, j, i - j): 1 for i in range(4) for j in range(1, i + 1)})
#Q[2, 1, 2] = 1
#Q[3, 2, 1] = 1


def solve(n, p, r):
    if r > p:
        return solve(n, r, p)
    # TODO: Base cases?
    print(n, p, r)
    if (n, p, r) in Q:
        return Q[n, p, r]
    if r == 1:
        Q[n, p, r] = sum(solve(k, p - 1, 1)
                         * combinations[n - 2, k - 1]
                         * factorials[n - k - 1]
                         for k in range(p - 1, n))
    else:
        Q[n, p, r] = sum(solve(k, p, 1)
                         * combinations[n - 1, k - 1]
                         * solve(n - k + 1, r, 1)
                         for k in range(p, n - r + 2))
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
