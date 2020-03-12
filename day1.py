def fuel(i):
    return i // 3 - 2


def total_fuel(i, prev_total):
    ret = fuel(i)
    if ret > 0:
        return total_fuel(ret, prev_total + ret)
    return prev_total


input = open("input/1").readlines()

# part 1
total = 0
for line in input:
    total += fuel(int(line))
print(total)

# part 2
total = 0
for line in input:
    total += total_fuel(int(line), 0)
print(total)
