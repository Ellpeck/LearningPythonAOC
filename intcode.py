def run(data, inputs=None, outputs=None):
    step = 0
    rel_base = 0
    while step < len(data):
        step, rel_base = run_step(data, step, inputs, outputs, rel_base)
        if step < 0:
            break
    return data[0]


def run_step(data, step, inputs=None, outputs=None, rel_base=0):
    entry = data[step]
    opcode = int(str(entry)[-2:])
    jump = 4
    if opcode == 99:
        return -1, rel_base
    elif opcode == 1:
        write_mode(data, entry, step, rel_base, 3, read_mode(data, entry, step, rel_base, 1) + read_mode(data, entry, step, rel_base, 2))
    elif opcode == 2:
        write_mode(data, entry, step, rel_base, 3, read_mode(data, entry, step, rel_base, 1) * read_mode(data, entry, step, rel_base, 2))
    elif opcode == 3:
        if inputs == None:
            print("Input value:")
            write_mode(data, entry, step, rel_base, 1, int(input()))
        else:
            if len(inputs) <= 0:
                return step, rel_base
            write_mode(data, entry, step, rel_base, 1, inputs.pop(0))
        jump = 2
    elif opcode == 4:
        res = read_mode(data, entry, step, rel_base, 1)
        if outputs == None:
            print(res)
        else:
            outputs.append(res)
        jump = 2
    elif opcode == 5:
        if read_mode(data, entry, step, rel_base, 1) != 0:
            step = read_mode(data, entry, step, rel_base, 2)
            jump = 0
        else:
            jump = 3
    elif opcode == 6:
        if read_mode(data, entry, step, rel_base, 1) == 0:
            step = read_mode(data, entry, step, rel_base, 2)
            jump = 0
        else:
            jump = 3
    elif opcode == 7:
        res = 1 if read_mode(data, entry, step, rel_base, 1) < read_mode(data, entry, step, rel_base, 2) else 0
        write_mode(data, entry, step, rel_base, 3, res)
    elif opcode == 8:
        res = 1 if read_mode(data, entry, step, rel_base, 1) == read_mode(data, entry, step, rel_base, 2) else 0
        write_mode(data, entry, step, rel_base, 3, res)
    elif opcode == 9:
        rel_base += read_mode(data, entry, step, rel_base, 1)
        jump = 2
    else:
        raise ValueError(opcode)
    return step + jump, rel_base


def write_data(data, index, val):
    # expand memory if necessary
    if index >= len(data):
        if val == 0:
            return
        data.extend([0 for x in range(len(data), index + 1)])
    data[index] = val


def get_data(data, index):
    if index >= len(data):
        return 0
    return data[index]


def get_mode(data, entry, offset):
    sEntry = str(entry)
    if len(sEntry) >= offset + 2:
        return int(sEntry[-offset - 2])
    return 0


def write_mode(data, entry, opcode_index, rel_base, offset, val):
    mode = get_mode(data, entry, offset)
    index = get_data(data, opcode_index + offset)
    if mode == 2:  # relative mode
        write_data(data, index + rel_base, val)
    else:  # immediate, position mode
        write_data(data, index, val)


def read_mode(data, entry, opcode_index, rel_base, offset):
    mode = get_mode(data, entry, offset)
    if mode == 1:  # immediate mode
        return get_data(data, opcode_index + offset)
    elif mode == 2:  # relative mode
        return get_data(data, get_data(data, opcode_index + offset) + rel_base)
    else:  # position mode
        return get_data(data, get_data(data, opcode_index + offset))
