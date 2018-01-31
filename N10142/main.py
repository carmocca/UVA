import sys


def get_winner(choices):
    points = [(choices.count(c), c) for c in set(choices)]
    max_points, winner = max(points)
    percentage = max_points / len(choices)
    return percentage, winner


def get_losers(choices):
    points = [(choices.count(c), c) for c in set(choices)]
    min_points, _ = min(points)
    losers = [p[1] for p in points if p[0] == min_points]
    return losers


def remove_losers(ballots, losers):
    aux = [[choice for choice in ballot if choice not in losers] for ballot in ballots]
    return [b for b in aux if b != []]


def solve(candidates, b):
    ballots = b
    while True:
        choices = [b[0] for b in ballots]
        percentage, winner = get_winner(choices)
        if percentage > 0.5:
            return [candidates[winner - 1]]
        losers = get_losers(choices)
        if set(choices) == set(losers):  # Tied
            return [candidates[i - 1] for i in losers]
        ballots = remove_losers(ballots, losers)


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for case in range(cases):
        n = int(file.readline())
        candidates = [file.readline().rstrip() for c in range(n)]
        ballots = []
        for line in file:
            if line.rstrip() == '':
                sol = solve(candidates, ballots)
                for candidate in sol:
                    res.append(candidate + '\n')
                break
            ballots.append([int(c) for c in line.split()])
        res.append('\n')
    res[-2] = res[-2].rstrip()
    return res[0: - 1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
