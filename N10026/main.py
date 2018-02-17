import sys


def solve(jobs):
    return [tup[0]
            for tup in sorted(
                [(i + 1, v) for i, v in enumerate(jobs)],
                key=lambda x: x[1][0] / x[1][1])]


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        n = int(file.readline())
        jobs = [tuple(int(x) for x in file.readline().split()) for _ in range(n)]
        res.append(' '.join(str(x) for x in solve(jobs)) + '\n')
        res.append('\n')
        file.readline()
    return res[:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
