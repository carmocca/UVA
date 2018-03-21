import sys
import collections

Table = collections.namedtuple('Table', ['id', 'capacity'])
Team = collections.namedtuple('Team', ['id', 'capacity'])


def solve(teams, tables):
    sorted_teams = sorted(
        (Team(i + 1, teams[i]) for i in range(len(teams))),
        key=lambda t: t.capacity, reverse=True)
    sorted_tables = sorted(
        (Table(i + 1, tables[i]) for i in range(len(tables))),
        key=lambda t: t.capacity, reverse=True)
    assigned_tables = []

    for team in sorted_teams:
        if team.capacity > len(sorted_tables):
            return (0)
        assigned_tables.append(
            (team.id, [t.id for t in sorted_tables[:team.capacity]]))

        sorted_tables = [Table(t.id, t.capacity - 1)
                         for t in sorted_tables[:team.capacity]
                         if t.capacity > 0] + sorted_tables[team.capacity:]

        sorted_tables = sorted(sorted_tables, reverse=True)

    print(sorted_teams)
    print(sorted_tables)
    print(assigned_tables)

    print(sorted(assigned_tables))
    print('\n')
    return (1, *[t[1] for t in sorted(assigned_tables, reverse=True)])


def main(file):
    res = []
    while True:
        m, n = [int(x) for x in file.readline().split()]
        if m == n == 0:
            return res
        teams = [int(x) for x in file.readline().split()]
        tables = [int(x) for x in file.readline().split()]
        sol = solve(teams, tables)
        res.append('{}\n'.format(sol[0]))
        res.extend(' '.join(map(str, x)) + '\n' for x in sol[1:])


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
