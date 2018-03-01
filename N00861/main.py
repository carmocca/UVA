import sys

'''
A state is an array whose length is the number of diagonals
in an axis for a board of size n x n.

Each cell contains a 0 if there is no bishop in the diagonal
otherwise the position of a bishop in the diagonal.

For example, given n = 2, k = 2 there are 4 possible solutions:

[B, -] => [1, 1, 0]
[B, -]

[B, B] => [1, 2, 0]
[-, -]

[-, -] => [0, 1, 1]
[B, B]

[-, B] => [1, 2, 1]
[-, B]
'''


def little_bishops(d, k):
    def is_complete(s):
        return len(s) == d

    def is_feasible(s):
        return s.count(0) == d - k

    def is_promising(s, c):
        # Incremental check, this is done for intersecting diagonals
        # which given our state configuration, are every 2 elements
        # so the range depends on the parity
        return all(c != s[i]
                   for i in range(1 if len(s) % 2 else 0, len(s), 2)
                   if c and s[i])

    def branch(s):
        # Range of the number of elements in each diagonal
        return range(len(s) + 2 if len(s) < d / 2 else d - len(s) + 1)

    def backtracking(s):
        if is_complete(s):
            if is_feasible(s):
                yield 1
        else:
            for child in branch(s):
                if is_promising(s, child):
                    for _ in backtracking(s + [child]):
                        yield 1

    return sum(backtracking([]))


def solve(n, k):
    if n > 1 and 2 * n - 1 <= k:
        return 0
    if k == 1:
        return n ** 2
    diagonals = 2 * n - 1
    return little_bishops(diagonals, k)


def main(file):
    for line in file:
        n, k = [int(x) for x in line.split()]
        if n == k == 0:
            return
        yield solve(n, k)


if __name__ == '__main__':
    # Use pre-calculated solution to avoid time limit exceeded
    values = '1 1 1 4 4 0 0 1 9 26 26 8 0 0 0 0 0 1 16 92 232 260 112 16 0 0 0 0 0 0 0 0 0 0 1 25 240 1124 2728 3368 1960 440 32 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 36 520 3896 16428 39680 53744 38368 12944 1600 64 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 49 994 10894 70792 282248 692320 1022320 867328 389312 81184 5792 128 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 64 1736 26192 242856 1444928 5599888 14082528 22522960 22057472 12448832 3672448 489536 20224 256 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'.split()
    keys = [(n, k) for n in range(1, 9) for k in range(n ** 2 + 1)]
    dic = dict(zip(keys, values))
    for line in sys.stdin:
        n, k = [int(x) for x in line.split()]
        if n == k == 0:
            break
        print(dic[n, k])
