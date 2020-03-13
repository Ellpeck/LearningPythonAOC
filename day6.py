class Planet:
    def __init__(self, name):
        self.name: str = name
        self.orbit_parent: Planet = None

    def count_orbits(self) -> int:
        if self.orbit_parent is not None:
            return self.orbit_parent.count_orbits() + 1
        return 0

    def collect_parents(self, coll) -> list:
        coll.append(self)
        if self.orbit_parent is not None:
            self.orbit_parent.collect_parents(coll)
        return coll


def collect_data() -> dict:
    data = open("input/6").readlines()
    planets = dict()
    for line in data:
        split = line.replace("\n", "").split(")")

        first = planets.get(split[0])
        if first is None:
            first = Planet(split[0])
            planets[first.name] = first

        second = planets.get(split[1])
        if second is None:
            second = Planet(split[1])
            planets[second.name] = second

        second.orbit_parent = first
    return planets


data = collect_data()

# part 1
total = 0
for planet in data.values():
    total += planet.count_orbits()
print(total)

# part 2
start: Planet = data["YOU"].orbit_parent
goal: Planet = data["SAN"].orbit_parent
start_parents = start.collect_parents([])
goal_parents = goal.collect_parents([])
for p in start_parents:
    if p in goal_parents:
        print(start_parents.index(p) + goal_parents.index(p))
        break
