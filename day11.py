import intcode


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 0

    def turn(self, rotation):
        if rotation == 1:
            self.direction += 1
            if self.direction > 3:
                self.direction = 0
        elif rotation == 0:
            self.direction -= 1
            if self.direction < 0:
                self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1

    def simulate(self, start_color):
        panels = {}
        step = 0
        rel_base = 0
        inputs = [start_color]
        outputs = []
        while step < len(data):
            step, rel_base = intcode.run_step(data, step, inputs, outputs, rel_base)
            if len(outputs) == 2:
                # color is first output
                panels[(self.x, self.y)] = outputs[0]
                # new direction is second output
                self.turn(outputs[1])
                self.move()

                outputs.clear()

                color = panels.get((self.x, self.y), 0)
                inputs.append(color)
            if step < 0:
                break
        return panels


with open("input/11") as f:
    raw_data = f.read().split(",")
data = list(map(lambda x: int(x), raw_data))


# part 1
robot = Robot()
print(len(robot.simulate(0)))

# part 2
robot = Robot()
panels = robot.simulate(1)

x1 = min(panels, key=lambda pos: pos[0])[0]
y1 = min(panels, key=lambda pos: pos[1])[1]
x2 = max(panels, key=lambda pos: pos[0])[0]
y2 = max(panels, key=lambda pos: pos[1])[1]
for y in range(y1, y2 + 1):
    for x in range(x1, x2 + 1):
        color = panels.get((x, y), 0)
        print("#" if color == 1 else " ", end="")
    print()
