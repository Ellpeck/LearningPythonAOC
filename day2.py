import intcode

input = open("input/2").read().split(",")
data = list(map(lambda i: int(i), input))

# part 1
p1 = data.copy()
p1[1] = 12
p1[2] = 2
print(intcode.run(p1))

# part 2
for i in range(0, 99):
    for j in range(0, 99):
        p2 = data.copy()
        p2[1] = i
        p2[2] = j
        if intcode.run(p2) == 19690720:
            print(100 * i + j)
            break
