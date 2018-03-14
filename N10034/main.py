import sys


def solve(freckles):
    pass

def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        n = int(file.readline())
        freckles = []
        for _ in range(n):
            x, y = [float(x) for x in file.readline().split()]
            freckles.append((x,y))
        file.readline()
        res.append("{}\n".format(solve(freckles)))
        res.append("\n")
    return res



if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')