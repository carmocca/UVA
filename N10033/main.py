import sys

def solve(instructions):
    registers = [000] * 10
    num_instructions = 0
    i = 0
    instruction = instructions[i]
    while instruction != '100':
        num_instructions += 1
        if instruction[0] == '0':
            if registers[int(instruction[2])] != 0:
                i = registers[int(instruction[1])]
                instruction = instructions[i]
                continue
        elif instruction[0] == '2':
            registers[int(instruction[1])] = int(instruction[2])
        elif instruction[0] == '3':
            registers[int(instruction[1])] = (registers[int(instruction[1])] + int(instruction[2])) % 1000
        elif instruction[0] == '4':
            registers[int(instruction[1])] = (registers[int(instruction[1])] * int(instruction[2])) % 1000
        elif instruction[0] == '5':
            registers[int(instruction[1])] = registers[int(instruction[2])]
        elif instruction[0] == '6':
            registers[int(instruction[1])] = (registers[int(instruction[1])] + registers[int(instruction[2])]) % 1000
        elif instruction[0] == '7':
            registers[int(instruction[1])] = (registers[int(instruction[1])] * registers[int(instruction[2])]) % 1000
        elif instruction[0] == '8':
            registers[int(instruction[1])] = instructions[registers[int(instruction[2])]]
        elif instruction[0] == '9':
            instructions[registers[2]] = registers[int(instruction[1])] 
        
        i += 1
        instruction = instructions[i]
    num_instructions += 1
    return num_instructions


def main(file):
    res = []
    cases = int(file.readline())
    file.readline()
    for case in range(cases):
        instructions = []
        while True:
            instruction = file.readline().rstrip() 
            if instruction == "":
                break
            instructions.append(instruction)
        instructions += ['000' for _ in range(len(instructions), 1000)]
        res.append(str(solve(instructions)) + '\n')
    return res

if __name__ == '__main__':
    res = main(sys.stdin)
    for line in res:
        print(line, end='')