import intcode

with open("input/13") as f:
    raw_data = f.read().split(",")
data = list(map(int, raw_data))

grid = {}

# part 1
step = 0
rel_base = 0
outputs = []
while step < len(data):
    step, rel_base = intcode.run_step(data, step, None, outputs, rel_base)
    if len(outputs) == 3:
        pos = (int(outputs[0]), int(outputs[1]))
        tile = int(outputs[2])
        grid[pos] = tile
        outputs.clear()
    if step < 0:
        break
print(len(list(filter(lambda x: x == 2, grid.values()))))
