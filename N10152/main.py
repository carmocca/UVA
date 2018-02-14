import sys


def solve(original, required):
    res = []
    print(original, required)
    return res


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        n = int(file.readline())
        original = [file.readline().rstrip() for _ in range(n)]
        required = [file.readline().rstrip() for _ in range(n)]
        res.extend(t + '\n' for t in solve(original, required))
        res.append('\n')
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
