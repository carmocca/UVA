import sys


def solve(n):
    p = n
    cont = 1
    while p != 1:
        if p % 10 == 1:
            p = (p - 1) // 10
            cont += 1
        else:
            p += n
    return cont


def main(file):
    return ['{}\n'.format(solve(int(line))) for line in file]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
