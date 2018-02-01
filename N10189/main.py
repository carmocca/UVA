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
    for i in range(rows):
        line = ''
        for j in range(cols):
            if field[i][j] == 1:
                line += '*'
                continue
            neighbours = get_neighbours(i, j, rows, cols)
            mines = sum(field[row][col] for (row, col) in neighbours)
            line += str(mines)
        res.append(line + '\n')
    return res


def main(file):
    res = []
    field_num = 1
    while True:
        (rows, cols) = [int(x) for x in file.readline().split()]
        if rows == cols == 0: break
        field = [[0 for col in range(cols)] for row in range(rows)]

        for i in range(rows):
            for j, char in enumerate(file.readline()):
                if char == '*':
                    field[i][j] = 1
        res.append("Field #{}:\n".format(field_num))
        res.extend(solve(field, rows , cols))
        res.append("\n")
        field_num += 1

    return res[0: -1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
