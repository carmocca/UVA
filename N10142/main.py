import sys


def get_first_choices(ballots):
    return [b[0] for b in ballots]


def get_points(choices):
    return {c: choices.count(c) for c in set(choices)}


def get_winner(points):
    winner = max(points, key=points.get)
    return winner, points[winner]


def get_losers(points):
    min_points = min(points.values())
    losers = [c for c, p in points.items() if p == min_points]
    return losers, min_points


def remove_losers(ballots, losers):
    return [[c for c in b if c not in losers] for b in ballots]


def update_points(points, losers, ballots):
    for loser in losers:
        del points[loser]

    '''
    Update the points incrementally. For each
    first choice loser increment the score of the next
    non-loser candidate
    '''
    for next_choices in [b[1:] for b in ballots if b[0] in losers]:
        for candidate in next_choices:
            if candidate in points:
                points[candidate] += 1
                break


def solve(candidates, b):
    ballots = b
    choices = get_first_choices(ballots)
    points = get_points(choices)
    while True:
        winner, max_points = get_winner(points)
        if max_points > sum(points.values()) / 2:  # Winner
            return [candidates[winner - 1]]

        losers, min_points = get_losers(points)
        if max_points == min_points:  # Tied
            return [candidates[i - 1] for i in losers]

        update_points(points, losers, ballots)
        ballots = remove_losers(ballots, losers)
        choices = get_first_choices(ballots)


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
                break
            ballots.append([int(c) for c in line.split()])
        for candidate in solve(candidates, ballots):
            res.append(candidate + '\n')
        res.append('\n')
    res[-2] = res[-2].rstrip()  # Remove last newline
    return res[0: -1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
