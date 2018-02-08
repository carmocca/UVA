import sys
import collections

graph = collections.defaultdict(set)
erdos_numbers = {}
ERDOS = 'Erdos, P.'


def build_graph(papers):
    global graph
    for paper in papers:
        for author in paper:
            graph[author].update(a for a in paper if a != author)


def calculate_erdos():
    global erdos_numbers
    # BFS
    visited, queue = set(), [(ERDOS, -1)]
    while queue:
        author, distance = queue.pop(0)
        if author not in visited:
            visited.add(author)
            erdos_numbers[author] = distance + 1
            for connected_author in graph[author] - visited:
                queue.append((connected_author, distance + 1))


def main(file):
    res = []
    cases = int(file.readline())
    for case in range(1, cases + 1):
        res.append('Scenario {}\n'.format(case))
        p, n = [int(x) for x in file.readline().split()]

        # Remove paper titles
        papers = [file.readline().split(':', 1)[0] for _ in range(p)]
        # Split every two commas
        papers = [zip(*[iter(p.split(','))] * 2) for p in papers]
        # Join zip tuples and trim
        papers = [[','.join(a).strip() for a in p] for p in papers]
        build_graph(papers)

        names = [file.readline().rstrip() for _ in range(n)]
        calculate_erdos()

        for name in names:
            res.append('{} {}\n'.format(name, erdos_numbers.get(name, 'infinity')))
    return res


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
