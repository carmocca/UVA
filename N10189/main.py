import sys


def get_neighbours(row, col, rows, cols):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < row + i < rows and -1 < col + j < cols:
                neighbours.append((row + i, col + j))
    return neighbours


def solve(field, rows, cols):
    res = []
    for row in range(rows):
        line = ''
        for col in range(cols):
            if field[row][col] == 1:
                line += '*'
                continue
            neighbours = get_neighbours(row, col, rows, cols)
            mines = sum(field[r][c] for r, c in neighbours)
            line += str(mines)
        res.append(line + '\n')
    return res


def main(file):
    res = []
    field_num = 1
    while True:
        rows, cols = [int(x) for x in file.readline().split()]
        if rows == cols == 0: break
        field = [[0 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col, char in enumerate(file.readline()):
                if char == '*':
                    field[row][col] = 1
        res.append('Field #{}:\n'.format(field_num))
        res.extend(solve(field, rows, cols))
        res.append('\n')
        field_num += 1
    return res[0: -1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
