import collections
import sys

Elephant = collections.namedtuple('Elephant', ['id', 'weight', 'iq'])


def solve(elephants):
    return [elephant.id for elephant in elephants]


def main(file):
    elephants = [Elephant(i + 1, *(int(x) for x in line.split()))
                 for i, line in enumerate(file)]
    return solve(elephants)


if __name__ == '__main__':
    sequence = main(sys.stdin)
    print(len(sequence))
    for elephant in sequence:
        print(elephant)
