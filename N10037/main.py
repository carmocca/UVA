import sys


def get_movements(waiting):
    people = len(waiting)
    if people == 1:
        return [[waiting.pop()]]
    elif people == 2:
        return [[waiting.pop(), waiting.pop()]]
    elif people == 3:
        fastest = waiting.pop(0)
        return [[fastest, waiting.pop()],
                [fastest],
                [fastest, waiting.pop()]]
    else:
        slowest = waiting.pop()
        snd_slowest = waiting.pop()
        if 2 * waiting[1] < waiting[0] + snd_slowest:
            return [[waiting[0], waiting[1]],
                    [waiting[0]],
                    [snd_slowest, slowest],
                    [waiting[1]]]
        else:
            return [[waiting[0], snd_slowest],
                    [waiting[0]],
                    [waiting[0], slowest],
                    [waiting[0]]]


def solve(crossing_times):
    total = 0
    movements = []
    waiting = sorted(crossing_times)
    while len(waiting):
        moves = get_movements(waiting)
        total += sum(max(m) for m in moves)
        movements.extend(moves)
    return total, movements


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        n = int(file.readline())
        crossing_times = [int(file.readline()) for _ in range(n)]
        total, movements = solve(crossing_times)
        res.append('{}\n'.format(total))
        res.extend('{}\n'.format(' '.join(str(p) for p in m)) for m in movements)
        res.append('\n')
        file.readline()
    return res[:-1]


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
