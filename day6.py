import sys

def countForPlanet(tree, origin, planet, depth):
	if (origin == planet):
		return depth
	if not(origin in tree):
		return 0
	count = 0
	for satellite in tree[origin]:
		count += countForPlanet(tree, satellite, planet, depth+1)
	return count


tree = {}
allPlanets = set()
with open("input6.txt") as fp:
 	for line in fp:
		planets = line.split(")")
		center = planets[0].strip()
		orbiting = planets[1].strip()

		allPlanets.add(center)
		allPlanets.add(orbiting)

		if center in tree:
			tree[center].append(orbiting)
		else:
			tree[center] = [orbiting]

count = 0
for planet in allPlanets:
	count += countForPlanet(tree, "COM", planet, 0)
print(count)
