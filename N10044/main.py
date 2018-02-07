import sys

def main(file):
    res = []
    cases = int(file.readline())
    for case in range(cases):
        papers = []
        names = []
        p, n = [file.readline().rstrip() for c in range(2)]
        for paper in range(p):
            papers.append(file.readline())
        for name in range(n):
            names.append(file.readline())
    return res

if __name__ = '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')