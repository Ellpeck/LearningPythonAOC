import intcode

with open("input/5") as f:
    puzzleInput = f.read().split(",")
data = list(map(lambda i: int(i), puzzleInput))

intcode.run(data)
