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


'''
def pdp(dp):
    for i, x in enumerate(dp):
        print(x)
        #print(([' ']*i) + x)
    print()


def solve2(cuts_input, l):
    cuts = [0] + cuts_input + [l]
    n = len(cuts)
    dp = [[float('inf')] * (n - i - 1) for i in range(n - 1)]

    for i in range(n - 1):
        dp[i][0] = 0

    for col in range(1, n - 1):
        for row in range(n - col - 1):

            print('col={}, row={}'.format(col, row))
            aux, dp[row][col] = dp[row][col], 'X'
            pdp(dp)
            dp[row][col] = aux

            x = sum(dp[row][0:col])
            min_ = min(x + dp[col + row - k][k] for k in range(col))
            print(x, min_, dp[row][col])
            #print('x:', x)
            #for k in range(col):
            #    x += dp[col + row - k][k]
            #print('x:', x)   
            if dp[row][col] > min_:
                dp[row][col] = min_
            #print(cuts, col, row)
            dp[row][col] += cuts[col + row + 1] - cuts[row]

    print('End')
    pdp(dp)
    return dp[0][n - 2]
'''
