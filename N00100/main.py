import sys


MEMOIZATION_SIZE = 1000000
cycle_len = [0] * MEMOIZATION_SIZE


def f(n_input):
    n = n_input
    length = 1
    while n != 1:
        if n < MEMOIZATION_SIZE and cycle_len[n] > 0:
            length = cycle_len[n] - 1
            n = 1 # break
        else:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            length += 1
    cycle_len[n] = length
    return length


def solve(x, y):
    if x > y: (x, y) = (y, x)
    max_length = 0
    for i in range(x, y + 1):
        length = f(i)
        if length > max_length: max_length = length
    return max_length


def main(file):
    res = []
    for line in file:
        (x, y) = [int(x) for x in line.split()]
        max_cycle_length = solve(x, y)
        res.append("{} {} {}\n".format(x, y, max_cycle_length))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
