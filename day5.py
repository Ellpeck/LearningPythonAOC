import intcode

puzzleInput = open("input/5").read().split(",")
data = list(map(lambda i: int(i), puzzleInput))

intcode.run(data)
