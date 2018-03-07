import sys

x, y, d = 0, 0, 0


def solve(a, b):
    global x, y, d
    if b == 0:
        x, y, d = 1, 0, a
    else:
        solve(b, a % b)
        x, y = y, x - y * (a // b)
    return x, y, d


def main(file):
    res = []
    for line in file:
        a, b = [int(x) for x in line.split()]
        res.append('{} {} {}\n'.format(*solve(a, b)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')