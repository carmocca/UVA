import sys


def flip(stack, pos):
    return stack[0:pos] + stack[pos:len(stack)][::-1]


def solve(stack):
    flips = []
    top = len(stack) - 1
    sorted_stack = sorted(stack, reverse=True)

    for i in range(top):
        if stack[i] == sorted_stack[i]:
            continue
        largest_pancake_pos = stack.index(sorted_stack[i])
        if largest_pancake_pos != top:
            stack = flip(stack, largest_pancake_pos)
            flips.append(largest_pancake_pos)
        stack = flip(stack, i)
        flips.append(i)

    flips.append(-1)
    return ' '.join(str(f + 1) for f in flips)


def main(file):
    res = []
    for line in file:
        stack = [int(x) for x in line.split()][::-1]
        res.append(line)
        res.append('{}\n'.format(solve(stack)))
    return res


if __name__ == '__main__':
    print(''.join(main(sys.stdin)), end='')
