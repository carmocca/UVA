import sys


def solve(original, required):
    N = len(original)
    # Simulate original as a bidirectional dict
    original_reversed = {t: p for p, t in original.items()}
    positions = [original_reversed[t] for t in [required[p]
                                                for p in range(N - 1, -1, -1)]]
    for i in range(N - 1):
        if positions[i] > positions[i + 1]:
            continue
        return [original[p] for p in positions[i+1:]]
    return []


def main(file):
    res = []
    cases = int(file.readline())
    for _ in range(cases):
        n = int(file.readline())
        original = {p: file.readline().rstrip() for p in range(n)}
        required = {p: file.readline().rstrip() for p in range(n)}
        res.extend(t + '\n' for t in solve(original, required))
        res.append('\n')
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
