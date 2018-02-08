import sys
import collections
import re
import pprint


def solve(dictionary, line):
    words_of_len = collections.defaultdict(list)
    possible_decodings = collections.defaultdict(set)
    found_decodings = {}

    '''
    Dict with keys as word lengths and a list of words in
    dictionary of that length as values
    '''
    for word in dictionary:
        words_of_len[len(word)].append(word)

    for encoded_word in line.split():
        words = words_of_len[len(encoded_word)]
        for i, char in enumerate(encoded_word):
            if len(words) == 1:  # Only one possible decoding for current char
                found_decodings[char] = set(words[0][i])
                # TODO: Remove decoded word?
            else:
                for w in words: # Add all possible decodings to that char
                    possible_decodings[char].add(w[i])

    decoded_chars = set.union(*found_decodings.values())
    decoded_chars_with_repetitions = [x for l in [list(v) for v in found_decodings.values()] for x in l] # Flatten
    if len(decoded_chars_with_repetitions) != len(decoded_chars):
        # There are conflicts with decoded chars thus no solution
        return re.sub(r'\S', '*', line)

    # Remove already decoded char from possible decodings
    for encoded_char in possible_decodings:
        possible_decodings[encoded_char].difference_update(decoded_chars)

    # Add found decodings of encoded chars
    possible_decodings.update(found_decodings)

    pprint.pprint(dict(possible_decodings))
    pprint.pprint(dict(found_decodings))
    return 'TODO'


def main(file):
    res = []
    n = int(file.readline())
    dictionary = [file.readline().rstrip() for _ in range(n)]
    for line in file:
        res.append(solve(dictionary, line.rstrip()) + '\n')
    return res


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
