import sys

res = [2, 5, 13]


def solve(n):
    if n > len(res):
        for i in range(len(res), n):
            res.append(2 * res[i - 1] + res[i - 2] + res[i - 3])
    return res[n - 1]


def main(file):
    return ['{}\n'.format(solve(int(line))) for line in file]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')