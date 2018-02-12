import sys

KNOWN_PHRASE = 'the quick brown fox jumps over the lazy dog'


def find_known_phrase(lines):
    for line in lines:
        if len(line) != len(KNOWN_PHRASE) or len(set(line)) != len(set(KNOWN_PHRASE)):
            continue
        for encoded, decoded in zip(line, KNOWN_PHRASE):
            if encoded != ' ' != decoded:
                return line
    return None


def get_decoding_mappings(line):
    return {encoded: decoded for encoded, decoded in zip(line, KNOWN_PHRASE)}


def solve(lines):
    encoded_phrase = find_known_phrase(lines)
    if not encoded_phrase:
        return ['No solution.']
    mappings = get_decoding_mappings(encoded_phrase)
    print(encoded_phrase, lines, mappings, '\n')
    return [''.join(mappings[c] for c in line) for line in lines]


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        lines = []
        for line in file:
            if line == '\n':
                break
            lines.append(line.rstrip())
        res = [l + '\n' for l in solve(lines)]
        res.append('\n')
    return res[0:-1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')