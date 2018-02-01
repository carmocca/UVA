import sys

matrix = [[0 for x in range(100)] for y in range(100)]


def solve(n, m):
    res = []
    for i in range(n):
        line = ''
        for j in range(m):
            if matrix[i][j] == 1:
                line += '*'
                continue
            mines = 0
            if j > 0 and i > 0 and matrix[i - 1][j - 1] == 1:
                mines += 1
            if j > 0 and matrix[i][j - 1] == 1:
                mines += 1
            if j > 0 and i < n and matrix[i + 1][j - 1] == 1:
                mines += 1
            if i > 0 and matrix[i - 1][j] == 1:
                mines += 1
            if i < n and matrix[i + 1][j] == 1:
                mines += 1
            if j < m and i > 0 and matrix[i - 1][j + 1] == 1:
                mines += 1
            if j < m and matrix[i][j + 1] == 1:
                mines += 1
            if j < m and i < n and matrix[i + 1][j + 1] == 1:
                mines += 1
            line += str(mines)
        res.append(line + '\n')

    return res


def main(file):
    res = []
    field = 1
    while True:
        (n, m) = [int(x) for x in file.readline().split()]
        if n == m == 0: break

        for i in range(n):
            for j, char in enumerate(file.readline()):
                if char == '*':
                    matrix[i][j] = 1
        res.append("Field #{}:\n".format(field))
        res.extend(solve(n , m))
        res.append("\n")
        field += 1

    return res[0: -1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
