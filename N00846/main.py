import sys
from math import floor
from math import sqrt

def solve(n):
    if n-1 < 0:
        return str(0)
    else:
        return str(floor( sqrt(n-1) + sqrt(n+1) ))

def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        x, y = [int(x) for x in file.readline().split()]
        res.append(solve(y - x) + '\n')
    return res

if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')