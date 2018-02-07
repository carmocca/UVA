import sys


# TODO: Use trie?
adjacency_matrix = {}
erdos_numbers = {}


def build_graph(papers):
    global adjacency_matrix
    for paper in papers:
        for author in paper:
            adjacency_matrix.setdefault(author, [])
            adjacency_matrix[author].extend(a for a in paper if a != author)
    adjacency_matrix.setdefault('Erdos P.', [])


def calculate_erdos(names):
    erdos_numbers.setdefault('Erdos P.', 0)
    for name in names:
        # TODO: BFS from Erdos
        pass


# TODO: Delete
def print_dict(d):
    for key, value in d.items():
        print('"{}" -> {}'.format(key, value))
    print()


def main(file):
    res = []
    cases = int(file.readline())
    for case in range(1, cases + 1):
        res.append('Scenario {}\n'.format(case))
        p, n = [int(x) for x in file.readline().split()]

        # Remove paper titles
        papers = [file.readline().split(':', 1)[0] for _ in range(p)]
        # Split every two commas
        papers = [zip(*[iter(p.split(','))]*2) for p in papers]
        # Join zip tuples and trim
        papers = [[''.join(a).strip() for a in p] for p in papers]
        build_graph(papers)

        print_dict(adjacency_matrix)

        names = [file.readline().rstrip() for _ in range(n)]
        calculate_erdos(names)

        print_dict(erdos_numbers)

        for name in names:
            res.append('{} {}\n'.format(
                name, erdos_numbers.get(name, 'infinity')))
    return res


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')

