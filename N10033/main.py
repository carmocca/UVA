import sys

halt = 100


def get_digit(number, n):
    return number // 10 ** n % 10


def execute(pointer, first, second, third):
    global registers
    global RAM
    if third == 0 and registers[first] != 0:
        return registers[second]
    elif third == 2:
        registers[second] = first
    elif third == 3:
        registers[second] += first
    elif third == 4:
        registers[second] *= first
    elif third == 5:
        registers[second] = registers[first]
    elif third == 6:
        registers[second] += registers[first]
    elif third == 7:
        registers[second] *= registers[first]
    elif third == 8:
        registers[second] = RAM[registers[first]]
    elif third == 9:
        RAM[registers[first]] = registers[second]
    registers[second] %= 1000
    return pointer + 1


def solve():
    pointer = 0
    executed = 0
    instruction = RAM[pointer]
    while instruction != halt:
        '''
        i.e. for instruction 123 first is 3, second is 2 and third is 1
        '''
        first = get_digit(instruction, 0)
        second = get_digit(instruction, 1)
        third = get_digit(instruction, 2)

        pointer = execute(pointer, first, second, third)
        executed += 1
        instruction = RAM[pointer]
    return executed + 1


def main(file):
    global registers
    global RAM
    res = []
    cases = int(file.readline())
    file.readline()
    for _ in range(cases):
        registers = [0] * 10
        RAM = [0] * 1000
        for i in range(1000):
            instruction = file.readline().rstrip()
            if instruction == '':
                break
            RAM[i] = int(instruction)
        res.append(str(solve()) + '\n')
        res.append('\n')
    return res[0: -1]


if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')
