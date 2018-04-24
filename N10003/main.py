import sys


def solve(cuts_input, l):
    cuts = [0] + cuts_input + [l]
    n = len(cuts) - 1
    dp = [[float('inf')] * n for i in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for col in range(1, n):
        for row in range(col - 1, -1, -1):
            min_ = min(dp[row][x] + dp[x + 1][col] for x in range(row, col))
            if dp[row][col] > min_:
                dp[row][col] = min_
            dp[row][col] += cuts[col + 1] - cuts[row]

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


''' Solution without empty cells
def solve(cuts_input, l):
    cuts = [0] + cuts_input + [l]
    n = len(cuts)
    dp = [[float('inf')] * (n - i - 1) for i in range(n - 1)]

    for i in range(n - 1):
        dp[i][0] = 0

    for col in range(1, n - 1):
        for row in range(n - col - 1):
            horizontal = dp[row][:col]
            # TODO: generate the list already reversed
            vertical = [dp[col + row - k][k] for k in range(col)]
            min_ = min(map(sum, zip(horizontal, reversed(vertical))))
            if dp[row][col] > min_:
                dp[row][col] = min_
            dp[row][col] += cuts[col + row + 1] - cuts[row]

    return dp[0][n - 2]
'''
