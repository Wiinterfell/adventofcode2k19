import sys

def neverDecrease(nb):
	for i in range(len(nb)-1):
		if (int(nb[i]) > int(nb[i+1])):
			return False
	return True

def twoConsecutive(nb):
	previous = ""
	previousNbOfMatches = 0
	for i in range(len(nb)):
		if (previous == nb[i]):
			previousNbOfMatches += 1
		else:
			if (previousNbOfMatches == 1):
				return True
			previous = nb[i]
			previousNbOfMatches = 0
	if (previousNbOfMatches == 1):
		return True
	return False

def meetCriteria(nb):
	return (neverDecrease(nb) and twoConsecutive(nb))

possibilities = 0
with open("input4.txt") as fp:
 	inputs = fp.readline().split("-")
 	lower = int(inputs[0])
 	upper = int(inputs[1])

 	for i in range(lower,upper):
 		if (meetCriteria(str(i))):
 			possibilities += 1

 	print(possibilities)