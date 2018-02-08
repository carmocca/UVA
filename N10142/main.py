import sys


def get_first_choices(ballots):
    return [b[0] for b in ballots]


def get_points(candidate_num, choices):
    return {c: choices.count(c) for c in range(1, candidate_num + 1)}


def get_winner(points):
    winner = max(points, key=points.get)
    return winner, points[winner]


def get_losers(points):
    min_points = min(points.values())
    losers = [c for c, p in points.items() if p == min_points]
    return losers, min_points


def remove_losers(ballots, losers):
    return [[c for c in b if c not in losers] for b in ballots]


def update_points(points, losers, ballots, choices):
    for loser in losers:
        del points[loser]
    '''
    Update the points incrementally. For each
    first choice loser increment the score of the next
    non-loser candidate
    '''
    for next_choice in [ballots[i][0] for i, c in enumerate(choices) if c in losers]:
        points[next_choice] += 1


def solve(candidates, b):
    ballots = b
    choices = get_first_choices(ballots)
    points = get_points(len(candidates), choices)
    while True:
        winner, max_points = get_winner(points)
        if 2 * max_points > sum(points.values()):  # Winner
            return [candidates[winner - 1]]

        losers, min_points = get_losers(points)
        if max_points == min_points:  # Tied
            return [candidates[i - 1] for i in losers]

        ballots = remove_losers(ballots, losers)
        update_points(points, losers, ballots, choices)
        choices = get_first_choices(ballots)


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
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
    return res[0: -1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
