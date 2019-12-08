import sys

def toStr(x,y):
	return str(x) + "." + str(y)

def getX(str):
	return int(str.split(".")[0])

def getY(str):
	return int(str.split(".")[1])

def manhattanDistance(x1,y1,x2,y2):
	return abs(x1-x2) + abs(y1-y2)

intersection = []
recordedPositions = set()
with open("input3.txt") as fp:
 	wire1 = fp.readline().split(",")
 	wire2 = fp.readline().split(",")

 	# mark path on grid
 	x = 0
 	y = 0
 	for direction in wire1:
 		nbSteps = int(direction[1:])
 		if (direction[0] == "R"):
 			for i in range(nbSteps):
 				x += 1
 				recordedPositions.add(toStr(x,y))
 		elif (direction[0] == "U"):
 			for i in range(nbSteps):
 				y += 1
 				recordedPositions.add(toStr(x,y))
 		elif (direction[0] == "L"):
 			for i in range(nbSteps):
 				x -= 1
 				recordedPositions.add(toStr(x,y))
 		elif (direction[0] == "D"):
 			for i in range(nbSteps):
 				y -= 1
 				recordedPositions.add(toStr(x,y))


 	# second wire: check intersection
  	x = 0
 	y = 0
 	for direction in wire2:
 		nbSteps = int(direction[1:])
 		if (direction[0] == "R"):
 			for i in range(nbSteps):
 				x += 1
 				if toStr(x,y) in recordedPositions:
 					intersection.append(toStr(x,y))
 		elif (direction[0] == "U"):
 			for i in range(nbSteps):
 				y += 1
 				if toStr(x,y) in recordedPositions:
 					intersection.append(toStr(x,y))
 		elif (direction[0] == "L"):
 			for i in range(nbSteps):
 				x -= 1
 				if toStr(x,y) in recordedPositions:
 					intersection.append(toStr(x,y))
 		elif (direction[0] == "D"):
 			for i in range(nbSteps):
 				y -= 1
 				if toStr(x,y) in recordedPositions:
 					intersection.append(toStr(x,y))


 	# find closest intersection
 	minDist = sys.maxint
 	for point in intersection:
 		dist = manhattanDistance(0,0,getX(point),getY(point))
 		if (dist < minDist):
 			minDist = dist

 
 	print(minDist)

		
