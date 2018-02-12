import sys

def solve(stack):
    res = ['0']
    return ' '.join(res)

def main(file):
    res = []
    while True:
        stack = [x for x in file.readline().split()]
        if len(stack) == 0:
            break
        res.append('{}\n'.format(' '.join(stack)))
        res.append('{}\n'.format(solve(stack)))
    return res

if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')