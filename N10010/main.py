import sys

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, 1)
DOWN = (0, -1)
UPPERRIGHT = (1, 1)
UPPERLEFT = (-1, 1)
LOWERRIGHT = (1, -1)
LOWERLEFT = (-1, -1)
DIRECTIONS = [RIGHT, LEFT, UP, DOWN, UPPERRIGHT, UPPERLEFT, LOWERRIGHT, LOWERLEFT]


def match(row, col, grid, word, rows, cols):
    if grid[row][col] != word[0]:
        return False
    for direction in DIRECTIONS:
        x, y = direction
        for i in range(len(word)):
            r = row + y * i
            c = col + x * i
            if c < 0 \
               or c >= cols \
               or r < 0 \
               or r >= rows \
               or grid[r][c] != word[i]:
                break
        else:
            # No breaks happened during the iteration
            return True


def solve(rows, cols, grid, word):
    for row in range(rows):
        for col in range(cols):
            ocurrence = match(row, col, grid, word, rows, cols)
            if ocurrence:
                return row + 1, col + 1


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        m, n = [int(x) for x in file.readline().split()]
        grid = [file.readline().rstrip().lower() for _ in range(m)]
        n_words = int(file.readline())
        words = [file.readline().rstrip().lower() for _ in range(n_words)]
        file.readline()
        for word in words:
            x, y = solve(m, n, grid, word)
            res.append('{} {}\n'.format(x, y))
        res.append('\n')
    return res[0:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')