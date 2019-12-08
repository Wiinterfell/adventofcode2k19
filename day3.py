import sys

def toStr(x,y):
	return str(x) + "." + str(y)

def getX(str):
	return int(str.split(".")[0])

def getY(str):
	return int(str.split(".")[1])

def manhattanDistance(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1-y2)

def moveForward(direction,x,y):
	if (direction == "R"):
 		x += 1
 	elif (direction == "U"):
 		y += 1
 	elif (direction == "L"):
 		x -= 1
 	elif (direction == "D"):
 		y -= 1
 	return x,y


intersection = []
intersectionSteps = []
recordedPositions = dict()
with open("input3.txt") as fp:
 	wire1 = fp.readline().split(",")
 	wire2 = fp.readline().split(",")

 	# mark path on grid
 	x = 0
 	y = 0
 	steps = 0
 	for direction in wire1:
 		nbSteps = int(direction[1:])
 		for i in range(nbSteps):
 			x,y = moveForward(direction[0],x,y)
 			steps += 1
 			recordedPositions[toStr(x,y)] = steps

 	# second wire: check intersection
  	x = 0
 	y = 0
 	steps2 = 0
 	for direction in wire2:
 		nbSteps = int(direction[1:])
 		for i in range(nbSteps):
 			x,y = moveForward(direction[0],x,y)
 			steps2 += 1
 			if toStr(x,y) in recordedPositions:
 				totalSteps = steps2 + recordedPositions[toStr(x,y)]
 				intersection.append(toStr(x,y))
 				intersectionSteps.append(totalSteps)

 	# find closest intersection
 	minDist = sys.maxint
 	for steps in intersectionSteps:
 		#dist = manhattanDistance(0,0,getX(point),getY(point))
 		if (steps < minDist):
 			minDist = steps

 
 	print(minDist)

		
