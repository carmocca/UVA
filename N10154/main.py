
import collections
import sys

Turtle = collections.namedtuple('Turtle', ['weight', 'strength'])


def solve(turtles):
    n = len(turtles)
    dp = [1e99] * n
    max_, dp[0] = 0, 0
    for turtle in sorted(turtles):
        for i in range(n - 1, -1, -1):
            if dp[i] + turtle.weight <= turtle.strength \
               and dp[i] + turtle.weight < dp[i + 1]:
                dp[i + 1] = dp[i] + turtle.weight
                max_ = max(max_, i + 1)
    return max_


def main(file):
    turtles = [Turtle(*(int(x) for x in line.split()))
               for line in file]
    return solve(turtles)


if __name__ == '__main__':
    print(main(sys.stdin))
