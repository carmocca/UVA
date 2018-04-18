import sys


def solve(cuts_input, l):
    cuts = [0] + cuts_input + [l]
    n = len(cuts)
    dp = [[float('inf')] * (n - i - 1) for i in range(n - 1)]

    for i, j in zip(range(n - 2, -1, -1), range(n)):
        dp[i][j] = 0

    for i in range(n-3, -1, -1):
        for k, j in zip(range(i, -1, -1), range(n)):
            for l, m in zip(range(n - 2 - j, k, -1), range(j + 1, n)):
                dp[k][j] = min(
                    dp[k][j],
                    dp[l][j] + dp[k][m] + cuts[n - 1 - k] - cuts[j])
    #import pprint
    # pprint.pprint(dp)
    return dp[0][0]


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
