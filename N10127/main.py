import sys


def append_1(n):
    return int(str(n) + '1')


def solve(n):
    p = 1
    while n > p:
        p = append_1(p)
    digits = len(str(p))
    while p > 0:
        while n > p:
            p = append_1(p)
            digits += 1
        p %= n
    return digits


def main(file):
    return ['{}\n'.format(solve(int(line))) for line in file]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
