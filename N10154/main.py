
import collections
import sys

Turtle = collections.namedtuple('Turtle', ['weight', 'strength'])


def solve(turtles):
    n = len(turtles)
    dp = [float('inf')] * n
    max_, dp[0] = 0, 0

    for weight, strength in sorted(turtles, key=lambda t: t.strength):
        for i in range(max_, -1, -1):
            if strength > dp[i] + weight < dp[i + 1]:
                dp[i + 1] = dp[i] + weight
                max_ = max(max_, i + 1)
    return max_


def main(file):
    turtles = [Turtle(*map(int, line.split())) for line in file]
    return solve(turtles)


if __name__ == '__main__':
    print(main(sys.stdin))
