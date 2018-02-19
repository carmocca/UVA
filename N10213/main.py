import sys


def solve(n):
    return (n**4 - 6 * n**3 + 23 * n**2 - 18 * n + 24) // 24


def main(file):
    file.readline()
    return ['{}\n'.format(solve(int(line))) for line in file]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')