def run(data, inputs=None, outputs=None):
    i = 0
    while i < len(data):
        i = run_step(data, i, inputs, outputs)
        if i < 0:
            break
    return data[0]


def run_step(data, step, inputs=None, outputs=None):
    entry = data[step]
    opcode = int(str(entry)[-2:])
    jump = 4
    if opcode == 99:
        return -1
    elif opcode == 1:
        data[data[step + 3]] = param_mode(data, entry, step, 1) + param_mode(data, entry, step, 2)
    elif opcode == 2:
        data[data[step + 3]] = param_mode(data, entry, step, 1) * param_mode(data, entry, step, 2)
    elif opcode == 3:
        if inputs == None:
            print("Input value: (1 for part 1, 5 for part 2)")
            data[data[step + 1]] = int(input())
        else:
            if len(inputs) <= 0:
                return step
            data[data[step + 1]] = inputs.pop(0)
        jump = 2
    elif opcode == 4:
        res = param_mode(data, entry, step, 1)
        if outputs == None:
            print(res)
        else:
            outputs.append(res)
        jump = 2
    elif opcode == 5:
        if param_mode(data, entry, step, 1) != 0:
            step = param_mode(data, entry, step, 2)
            jump = 0
        else:
            jump = 3
    elif opcode == 6:
        if param_mode(data, entry, step, 1) == 0:
            step = param_mode(data, entry, step, 2)
            jump = 0
        else:
            jump = 3
    elif opcode == 7:
        res = 1 if param_mode(data, entry, step, 1) < param_mode(data, entry, step, 2) else 0
        data[data[step + 3]] = res
    elif opcode == 8:
        res = 1 if param_mode(data, entry, step, 1) == param_mode(data, entry, step, 2) else 0
        data[data[step + 3]] = res
    else:
        raise ValueError(opcode)
    return step + jump


def param_mode(data, entry, opcodeIndex, offset):
    sEntry = str(entry)
    if len(sEntry) >= offset + 2:
        mode = int(sEntry[-offset - 2])
        if mode == 1:
            return data[opcodeIndex + offset]
    return data[data[opcodeIndex + offset]]
