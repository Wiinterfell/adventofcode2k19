import sys

total_fuel = 0
with open("input1.txt") as fp:
 	for line in fp:
		fuel = int(line)
		while (fuel > 0):
			fuel = fuel / 3 - 2
			if (fuel > 0):
				total_fuel += fuel
print(total_fuel)