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

def pathForPlanet(tree, origin, planet, path):
	if (origin == planet):
		return path
	if not(origin in tree):
		return []
	for satellite in tree[origin]:
		newPath = list(path)
		newPath.append(satellite)
		resultPath = pathForPlanet(tree, satellite, planet, newPath)
		if (len(resultPath) > 0):
			return resultPath
	return []

def findClosestCommonCenter(youPath, sanPath):
	i = 0
	while(youPath[i] == sanPath[i]):
		i += 1
	return youPath[i-1]


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

youPath = pathForPlanet(tree, "COM", "YOU", [])
sanPath = pathForPlanet(tree, "COM", "SAN", [])
closestCommonCenter =findClosestCommonCenter(youPath, sanPath)
distance = countForPlanet(tree, closestCommonCenter, "YOU", 0) + countForPlanet(tree, closestCommonCenter, "SAN", 0) - 2 # SAN and YOU aren't orbit transfers
print(distance)

