import sys


def solve(x, z):
    nx, nz = len(x), len(z)
    # Size |X| x |Z|. Could be |X| x 2
    dp = [[0 for j in range(nx)] for i in range(nz)]

    for j in range(nx):
        if x[j] == z[0]:
            dp[0][j] = 1

    for i in range(1, nz):
        counter = 0
        for j in range(i, nx):
            counter += dp[i - 1][j - 1]
            if z[i] == x[j]:
                dp[i][j] = counter

    return sum(dp[nz - 1][j] for j in range(nx))


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        x = file.readline().rstrip()
        z = file.readline().rstrip()
        res.append('{}\n'.format(solve(x, z)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
