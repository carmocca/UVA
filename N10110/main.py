import sys
import math


def solve(n):
    return 'yes' if math.sqrt(n).is_integer() else 'no'


def main(file):
    res = []
    for line in file:
        n = int(line)
        if n:
            res.append('{}\n'.format(solve(n)))
        else:
            return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
