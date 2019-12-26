import sys

userInput = 1

with open("input5.txt") as fp:
 	instr_str = fp.readline().split(",")
 	instr = list(map(int, instr_str))

	index = 0
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
		if (opcode in (1, 2)):
			if (secondParamMode == 0):
				secondNb = instr[instr[index+2]]
			else:
				secondNb = instr[index+2]
			res_position = instr[index+3]

		# compute result of instruction
		res = 0
		if opcode == 1:
			res = firstNb + secondNb
			instr[res_position] = res
			index += 4
		elif opcode == 2:
			res = firstNb * secondNb
			instr[res_position] = res
			index += 4
		elif opcode == 3:
			instr[instr[index+1]] = userInput
			index += 2
		elif opcode == 4:
			if (firstNb != 0):
				print(firstNb)
				break
			index += 2
		else:
			print("error " + str(opcode))
			break