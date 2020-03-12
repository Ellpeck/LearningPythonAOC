def fits(num, max_group_size):
    for i in range(0, len(num) - 1):
        if int(num[i + 1]) < int(num[i]):
            return False

    inc = False
    i = 0
    while i < len(num):
        group = 1
        for j in range(1, len(num) - i):
            if num[i] == num[i + j]:
                group += 1
        if group >= 2 and group <= max_group_size:
            inc = True
        i += group
    return inc


input = open("input/4").read().split("-")
lowest = int(input[0])
highest = int(input[1])

total1 = 0
total2 = 0
for num in range(lowest, highest):
    if fits(str(num), 6):
        total1 += 1
    if fits(str(num), 2):
        total2 += 1
print(total1)
print(total2)
