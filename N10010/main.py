import sys

def upleft(i, j, letters, w):
    for k in range(1, len(w)):
        if i-k < 0 or j-k < 0 or letters[i-k][j-k] != w[k]:
            return False
    return True

def up(i, j, letters, w):
    for k in range(1, len(w)):
        if i-k < 0 or letters[i-k][j] != w[k]:
            return False
    return True

def upright(i, j, letters, w):
    for k in range(1, len(w)):
        if i-k < 0 or j+k >= len(letters[i]) or letters[i-k][j+k] != w[k]:
            return False
    return True

def left(i, j, letters, w):
    for k in range(1, len(w)):
        if j-k < 0 or letters[i][j-k] != w[k]:
            return False
    return True

def right(i, j, letters, w):
    for k in range(1, len(w)):
        if j+k >= len(letters[i]) or letters[i][j+k] != w[k]:
            return False
    return True

def downleft(i, j, letters, w):
    for k in range(1, len(w)):
        if i+k >= len(letters) or j-k < 0 or letters[i+k][j-k] != w[k]:
            return False
    return True

def down(i, j, letters, w):
    for k in range(1, len(w)):
        if i+k >= len(letters) or letters[i+k][j] != w[k]:
            return False
    return True

def downright(i, j, letters, w):
    for k in range(1, len(w)):
        if i+k >= len(letters) or j+k >= len(letters[i]) or letters[i+k][j+k] != w[k]:
            return False
    return True

def match(i, j, letters, word):
    w = list(word)
    if letters[i][j] != w[0]:
        return False
    return upleft(i, j, letters, w) or up(i, j, letters, w) or upright(i, j, letters, w) or \
            left(i, j, letters, w) or right(i, j, letters, w) or \
            downleft(i, j, letters, w) or down(i, j, letters, w) or downright(i, j, letters, w)


def solve(m, n, letters, words):
    res = [(0,0)] * len(words)
    solved = []
    for i in range(m):
        for j in range(n):
            for k, word in enumerate(words):
                if res[k] == (0,0):
                    ocurrence = match(i, j, letters, word)
                    if ocurrence:
                        res[k] = (i+1, j+1)
                        solved.append(word)
    return res


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        m, n = [int(x) for x in file.readline().split()]
        letters = [[letter.lower() for letter in list(file.readline().rstrip())] for _ in range(m)]
        n_words = int(file.readline())
        words = [file.readline().rstrip().lower() for _ in range(n_words)]
        file.readline()
        for ocurrence in solve(m, n, letters, words):
            res.append('{} {}\n'.format(ocurrence[0], ocurrence[1]))
        res.append('\n')
    return res[0: -1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')