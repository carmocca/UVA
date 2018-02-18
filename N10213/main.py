import sys

def solve(n):
    res = 1
    # Number of lines
    if n > 0:
        res += (n * (n - 1)) // 2
    #Number of intersections
    if n > 2:
        res += ((n-3) * (n-2) * (n-1) * n) // 24
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