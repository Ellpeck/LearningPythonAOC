import intcode

with open("input/9") as f:
    raw_data = f.read().split(",")
data = list(map(lambda x: int(x), raw_data))

# part 1
intcode.run(data, [1])

# part 2
intcode.run(data, [2])
