import sys


def solve(n):
    pass


def main(file):
    return ['{}\n'.format(solve(int(line))) for line in file if line != '0\n']


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')