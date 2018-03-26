import sys
import collections

# Team/Table
T = collections.namedtuple('T', ['size', 'id'])


def solve(teams, tables):
    teams_by_size = sorted((T(size, id + 1) for id, size in enumerate(teams)), reverse=True)
    available_tables = sorted((T(size, id + 1) for id, size in enumerate(tables)), reverse=True)

    team_tables = []
    for team in teams_by_size:
        if team.size > len(available_tables):
            # The team doesn't fit in the available tables
            return None
        # Set the team's assigned tables
        team_tables.append((team.id, [table.id for table in available_tables[:team.size]]))
        unassigned = available_tables[team.size:]
        # Update recently occupied tables' sizes
        available_tables = [T(table.size - 1, table.id) for table in available_tables[:team.size]]
        # Filter out full tables
        available_tables = [table for table in available_tables if table.size > 0]
        # Sort by available space again
        available_tables = sorted(available_tables + unassigned, reverse=True)

    return [t[1] for t in sorted(team_tables)]


def main(file):
    res = []
    while True:
        m, n = [int(x) for x in file.readline().split()]
        if m == n == 0:
            return res
        teams = [int(x) for x in file.readline().split()]
        tables = [int(x) for x in file.readline().split()]
        sol = solve(teams, tables)
        res.append((0, 0) if sol is None else (1, sol))


if __name__ == '__main__':
    for valid, sol in main(sys.stdin):
        print(valid)
        if valid:
            for x in sol:
                print(' '.join(map(str, x)))
