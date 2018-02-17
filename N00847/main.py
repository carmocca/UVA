import sys

OLLIE = 'Ollie wins.'
STAN = 'Stan wins.'


def solve(n):
    multiplier = 9
    winner = STAN
    p = 1
    while True:
        p *= multiplier
        if p >= n:
            return winner
        multiplier = 9 if multiplier is 2 else 2
        winner = STAN if winner is OLLIE else OLLIE


def main(file):
    return ['{}\n'.format(solve(int(line))) for line in file]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
