import intcode


def combinations(remaining: list, progress: list = []):
    if len(remaining) <= 0:
        return [progress]
    total = []
    for i in remaining:
        total += combinations([x for x in remaining if x != i], progress + [i])
    return total


with open("input/7") as f:
    raw_data = f.read().split(",")
data = list(map(lambda x: int(x), raw_data))

# part 1
highest = 0
for combination in combinations(range(0, 5)):
    output = [0]
    for i in combination:
        d = data.copy()
        intcode.run(d, [i, output[-1]], output)
    if output[-1] > highest:
        highest = output[-1]
print(highest)

# part 2
highest = 0
for combination in combinations(range(5, 10)):
    datas = [data.copy() for x in combination]
    steps = [0 for x in combination]
    throughputs = [[combination[i]] for i in range(0, len(combination))]
    throughputs[0].append(0)
    done = 0
    while done < len(combination):
        for i in range(0, len(combination)):
            if steps[i] < 0:
                continue
            steps[i] = intcode.run_step(datas[i], steps[i], throughputs[i], throughputs[(i + 1) % len(combination)])
            if steps[i] < 0:
                done += 1
    if throughputs[0][0] > highest:
        highest = throughputs[0][0]
print(highest)
