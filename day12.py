import re
from copy import deepcopy
from itertools import combinations
from math import gcd


class Planet:
    def __init__(self, x, y, z):
        self.pos = list(map(int, [x, y, z]))
        self.motion = [0] * 3

    def apply_gravity(self, other):
        for i in range(3):
            self.motion[i] -= sign(self.pos[i] - other.pos[i])

    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.motion[i]

    def calc_energy(self):
        # add the absolute values of all dimensions together
        potential = sum(map(abs, self.pos))
        kinetic = sum(map(abs, self.motion))
        return potential * kinetic


def sign(num):
    if num == 0:
        return 0
    if num > 0:
        return 1
    return -1


def simulate_step(planets):
    # gravity
    # starting to be a bit more pythonian with these fancy methods
    for m1, m2 in combinations(planets, 2):
        m1.apply_gravity(m2)
        m2.apply_gravity(m1)
    # velocity
    for m in planets:
        m.apply_velocity()


def lcm(a, b):
    # https://en.wikipedia.org/wiki/Least_common_multiple
    return abs(a * b) // gcd(a, b)


planets = []
with open("input/12") as f:
    data = f.readlines()
for line in data:
    # trying to match <x=1, y=2, z=-9>
    match = re.search(r"<x=(-?\d+), y=(-?\d+), z=(-?\w+)>", line)
    planets.append(Planet(match.group(1), match.group(2), match.group(3)))

# part 1
part_1 = deepcopy(planets)
for _i in range(1000):
    simulate_step(part_1)
print(sum(map(Planet.calc_energy, part_1)))

# part 2
# what we want to do is this:
# simulate each coordinate individually for all planets combined
# and take the least common multiple of all of those steps
dimension_steps = [0] * 3
for i in range(3):
    part_2 = deepcopy(planets)
    original_pos = [p.pos[i] for p in part_2]
    while True:
        simulate_step(part_2)
        dimension_steps[i] += 1
        # have we arrived at the start position yet?
        if [p.pos[i] for p in part_2] == original_pos and [p.motion[i] for p in part_2] == [0] * len(part_2):
            break
print(lcm(lcm(dimension_steps[0], dimension_steps[1]), dimension_steps[2]))
