import sys

KNOWN_PHRASE = 'the quick brown fox jumps over the lazy dog'


def solve(phrases):
    for phrase in phrases:
        if len(phrase) != len(KNOWN_PHRASE):
            continue
        mappings = {}
        for encoded, decoded in zip(phrase, KNOWN_PHRASE):
            if encoded != ' ' == decoded \
               or encoded in mappings \
               and decoded != mappings[encoded]:
                break
            mappings[encoded] = decoded
        else:
            return [''.join(mappings[c] for c in p) for p in phrases]
    return ['No solution.']


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        phrases = []
        for line in file:
            if line == '\n':
                break
            phrases.append(line.rstrip())
        res.extend(l + '\n' for l in solve(phrases))
        res.append('\n')
    return res[0:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
