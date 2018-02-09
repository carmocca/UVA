import sys
import collections


def can_match(word, encoded, decodings):
    return len(word) == len(encoded) and \
           all(decodings[e] == w for w, e in zip(word, encoded) if decodings[e])


def new_decodings(word, encoded, decodings_input):
    decodings = decodings_input.copy()
    for w, e in zip(word, encoded):
        if decodings[e] == w:
            continue
        if decodings[e] is not None or w in decodings.values():
            return None
        decodings[e] = w
    return decodings


def backtracking(dictionary, encoded_words, decodings_input):
    encoded = encoded_words[0]
    for word in dictionary[len(encoded)]:
        match = can_match(word, encoded, decodings_input)
        decodings = new_decodings(word, encoded, decodings_input)
        if not match or not decodings:
            continue
        if len(encoded_words) == 1:  # End
            return [word]
        sol = backtracking(dictionary, encoded_words[1:], decodings)
        if sol:
            return [word] + sol
    return None


def solve(dictionary, encoded_words):
    characters = [c for l in [list(e) for e in encoded_words] for c in l]
    decodings = {ch: None for ch in set(characters)}
    res = backtracking(dictionary, encoded_words, decodings)
    if not res:
        res = ['*' * len(e) for e in encoded_words]
    return ' '.join(res)


def main(file):
    res = []
    n = int(file.readline())
    '''
    Dict with keys as word lengths and a list of words in
    dictionary of that length as values
    '''
    dictionary = collections.defaultdict(list)
    for _ in range(n):
        word = file.readline().rstrip()
        dictionary[len(word)].append(word)

    for line in file:
        encoded_words = line.rstrip().split()
        res.append(solve(dictionary, encoded_words) + '\n')
    return res


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
