#include <stdio.h>
#include <limits.h>

int dp[52][52];

int solve(int cuts[], int size, int l)
{
    int row, col, n;
    int x, min, value;

    n = size + 1;
    cuts[0] = 0;
    cuts[n] = l;

    for (x = 0; x < n; x++) {
        dp[x][x] = 0;
    }

    for (col = 1; col < n; col++) {
        for (row = col - 1; row >= 0; row--) {
            min = INT_MAX;
            for (x = row; x < col; x++) {
                value = dp[row][x] + dp[x + 1][col];
                if (value < min) {
                    min = value;
                }
            }
            dp[row][col] = min + cuts[col + 1] - cuts[row];
        }
    }

    return dp[0][n - 1];
}

int main()
{
    int l, n, cut;
    int cuts[52];

    while (1) {
        scanf("%d\n", &l);
        if (l == 0) {
            break;
        }
        scanf("%d\n", &n);
        for (cut = 1; cut <= n; cut++) {
            scanf("%d", &cuts[cut]);
        }
        printf("The minimum cutting is %d.\n", solve(cuts, n, l));
    }
}