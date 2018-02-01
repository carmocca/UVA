import sys

MEMOIZATION_SIZE = 1000000
cycle_len = [0] * MEMOIZATION_SIZE


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def get_cycle_length(n_input):
    n = n_input
    length = 1
    while n != 1:
        if n < MEMOIZATION_SIZE and cycle_len[n] > 0:
            length = cycle_len[n] - 1
            n = 1  # break
        else:
            n = collatz(n)
            length += 1
    cycle_len[n] = length
    return length


def solve(x, y):
    if x > y: x, y = y, x
    max_length = 0
    for i in range(x, y + 1):
        length = get_cycle_length(i)
        max_length = max(length, max_length)
    return max_length


def main(file):
    res = []
    for line in file:
        x, y = [int(x) for x in line.split()]
        res.append('{} {} {}\n'.format(x, y, solve(x, y)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
