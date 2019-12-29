import sys
import itertools

def runInstr(instr, firstInput, secondInput):
	index = 0
	usedFirstInput = False
	while(instr[index] != 99):
		opcode = instr[index] % 100
		# get modes for parameters
		firstParamMode = instr[index] / 100 % 10
		secondParamMode = instr[index] / 1000 % 10

		# get parameters according to the modes
		if (firstParamMode == 0):
			firstNb = instr[instr[index+1]]
		else:
			firstNb = instr[index+1]
		if (opcode in (1, 2, 5, 6, 7, 8)):
			if (secondParamMode == 0):
				secondNb = instr[instr[index+2]]
			else:
				secondNb = instr[index+2]
			res_position = instr[index+3]

		# compute result of instruction
		if opcode == 1:
			res = firstNb + secondNb
			instr[res_position] = res
			index += 4
		elif opcode == 2:
			res = firstNb * secondNb
			instr[res_position] = res
			index += 4
		elif opcode == 3:
			if (usedFirstInput):
				instr[instr[index+1]] = secondInput
			else:
				instr[instr[index+1]] = firstInput
				usedFirstInput = True
			index += 2
		elif opcode == 4:
			if (firstNb != 0):
				return firstNb
			index += 2
		elif opcode == 5:
			if (firstNb != 0):
				index = secondNb
			else:
				index += 3
		elif opcode == 6:
			if (firstNb == 0):
				index = secondNb
			else:
				index += 3
		elif opcode == 7:
			if (firstNb < secondNb):
				res = 1
			else:
				res = 0
			instr[res_position] = res
			index += 4
		elif opcode == 8:
			if (firstNb == secondNb):
				res = 1
			else:
				res = 0
			instr[res_position] = res
			index += 4
		else:
			print("error " + str(opcode))
			return 0
	return 0


userInput = 0
with open("input7.txt") as fp:
	instrStr = fp.readline().split(",")
 	instr = list(map(int, instrStr))

maxOutput = 0
settings = [0,1,2,3,4]
for permutation in (itertools.permutations(settings, 5)):
	secondInput = userInput
	for i in range(5):
		instrCopy = list(instr)
		secondInput = runInstr(instrCopy, permutation[i], secondInput)
	if (secondInput > maxOutput):
		maxOutput = secondInput
print(maxOutput)

