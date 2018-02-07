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


def calculate_erdos():
    global erdos_numbers
    erdos_numbers.setdefault('Erdos, P.', 0)
    visited = ['Erdos, P.']
    not_visited = adjacency_matrix['Erdos, P.']
    number = 1
    while len(not_visited) > 0:
        next_names = []
        for name in not_visited:
            erdos_numbers[name] = number
            visited.append(name)
            next_names += [n for n in adjacency_matrix[name] if n not in visited]
        number += 1
        not_visited = next_names




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
        papers = [[','.join(a).strip() for a in p] for p in papers]
        build_graph(papers)

        names = [file.readline().rstrip() for _ in range(n)]
        calculate_erdos()

        for name in names:
            res.append('{} {}\n'.format(
                name, erdos_numbers.get(name, 'infinity')))
    return res


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')

