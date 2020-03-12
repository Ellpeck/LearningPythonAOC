def run(data):
    i = 0
    while i < len(data):
        entry = data[i]
        opcode = int(str(entry)[-2:])
        jump = 4
        if opcode == 99:
            break
        elif opcode == 1:
            data[data[i + 3]] = param_mode(data, entry, i, 1) + param_mode(data, entry, i, 2)
        elif opcode == 2:
            data[data[i + 3]] = param_mode(data, entry, i, 1) * param_mode(data, entry, i, 2)
        elif opcode == 3:
            print("Input value: (1 for part 1, 5 for part 2)")
            data[data[i + 1]] = int(input())
            jump = 2
        elif opcode == 4:
            print(param_mode(data, entry, i, 1))
            jump = 2
        elif opcode == 5:
            if param_mode(data, entry, i, 1) != 0:
                i = param_mode(data, entry, i, 2)
                jump = 0
            else:
                jump = 3
        elif opcode == 6:
            if param_mode(data, entry, i, 1) == 0:
                i = param_mode(data, entry, i, 2)
                jump = 0
            else:
                jump = 3
        elif opcode == 7:
            res = 1 if param_mode(data, entry, i, 1) < param_mode(data, entry, i, 2) else 0
            data[data[i + 3]] = res
        elif opcode == 8:
            res = 1 if param_mode(data, entry, i, 1) == param_mode(data, entry, i, 2) else 0
            data[data[i + 3]] = res
        else:
            raise ValueError(opcode)
        i += jump


def param_mode(data, entry, opcodeIndex, offset):
    sEntry = str(entry)
    if len(sEntry) >= offset + 2:
        mode = int(sEntry[-offset - 2])
        if mode == 1:
            return data[opcodeIndex + offset]
    return data[data[opcodeIndex + offset]]


puzzleInput = open("input/5").read().split(",")
data = list(map(lambda i: int(i), puzzleInput))

run(data)
