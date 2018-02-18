import sys
from math import factorial

def solve(n):
    res = 1
    # Number of lines
    if n > 1:
        res += (n * (n - 1)) / 2
    #Number of intersections
    if n > 4:
        res += factorial(n) / (factorial(4) * factorial(n-4))
    return int(res)

def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        n = int(file.readline())
        res.append(str(solve(n)) + '\n')
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')