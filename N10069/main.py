import sys


def solve(x, z):
    nx, nz = len(x), len(z)
    pd = {(i, j): 0 for i in range(nz) for j in range(nx)}
    pd.update({(0, j): 1 for j in range(nx) if x[j] == z[0]})

    for i in range(nz - 1):
        for j in range(nx - 1):
            if pd[i, j] > 0:
                for k in range(j + 1, nx):
                    if z[i + 1] == x[k]:
                        pd[i + 1, k] += pd[i, j]

    return sum(pd[nz - 1, i] for i in range(nx))


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
