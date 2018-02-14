import sys


def solve(days, hartals):
    hartal_days = set()
    for hartal in hartals:
        for day in range(hartal - 1, days, hartal):
            if day % 7 not in [5, 6]:
                hartal_days.add(day)
    return len(hartal_days)


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        days = int(file.readline())
        parties = int(file.readline())
        hartals = []
        for _ in range(parties):
            hartals.append(int(file.readline()))
        res.append(str(solve(days, hartals)) + '\n')
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
