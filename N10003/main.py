import sys


dp = [[0] * 52 for i in range(52)]


def solve(cuts_input, l):
    cuts = [0] + cuts_input + [l]
    n = len(cuts) - 1

    for i in range(n):
        dp[i][i] = 0

    for col in range(1, n):
        for row in range(col - 1, -1, -1):
            dp[row][col] = (min(dp[row][x] + dp[x + 1][col]
                                for x in range(row, col))
                            + cuts[col + 1]
                            - cuts[row])

    return dp[0][n - 1]


def main(file):
    res = []
    while True:
        l = int(file.readline())
        if not l:
            break
        n = int(file.readline())
        sol = solve([int(x) for x in file.readline().split()], l)
        res.append('The minimum cutting is {}.\n'.format(sol))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
