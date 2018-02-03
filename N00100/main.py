import sys

cycle_len = {}


def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def get_cycle_length(n_input):
    global cycle_len
    n = n_input
    length = 1
    if n in cycle_len:
        return cycle_len[n]
    while n != 1:
        n = collatz(n)
        length += 1
    cycle_len[n_input] = length
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
