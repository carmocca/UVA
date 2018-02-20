import sys

def solve(x, y)
    pass

def main(input):
    res = []
    cases = int(file.readline())
    for _ in cases:
        x, y = [int(x) for x in file.readline().split()]
        res.append(solve(x, y) + '\n')
    return res

if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')