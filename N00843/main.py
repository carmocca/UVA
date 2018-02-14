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
            return {encoded: word}
        sol = backtracking(dictionary, encoded_words[1:], decodings)
        if sol:
            sol.update({encoded: word})
            return sol
    return None


def solve(dictionary, encoded_words):
    characters = [c for l in [list(e) for e in encoded_words] for c in l]
    decodings = {ch: None for ch in set(characters)}
    '''
    We can prune the backtracking tree by sorting the words by
    decreasing length, so that each word decodes more characters
    as well as removing duplicates
    '''
    ew_sorted = sorted(set(encoded_words), key=len, reverse=True)
    res = backtracking(dictionary, ew_sorted, decodings)
    res = ['*' * len(e) for e in encoded_words] if not res else [res[e] for e in encoded_words]
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
    print(''.join(main(sys.stdin)), end='')
