import sys

x = 0; y = 0; d = 0

def solve(a, b):
    global x, y, d
    if b == 0:
        x = 1; y = 0; d = a
    else:
        solve(b, a%b)
        _x = x
        x = y
        y = _x - y * (a//b)

def main(file):
    res = []
    for line in file:
        a, b = [int(x) for x in line.split()]
        solve(a, b)
        res.append('{} {} {}\n'.format(int(x), int(y), int(d)))
    return res

if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')