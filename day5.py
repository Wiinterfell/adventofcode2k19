import sys

userInput = 1

with open("input5.txt") as fp:
 	instr_str = fp.readline().split(",")
 	instr = list(map(int, instr_str))


	index = 0
	while(instr[index] != 99):
		nb_str = str(instr[index])
		opcode = nb_str[-1]
		print(opcode)

		# get modes for parameters
		firstParamMode = 0
		if (len(nb_str) > 2):
			firstParamMode = nb_str[-3]		
		secondParamMode = 0
		if (len(nb_str) > 3):
			secondParamMode = nb_str[-4]	
		thirdParamMode = 0

		# get parameters according to the modes
		if (firstParamMode == 0):
			firstNb = instr[instr[index+1]]
		else:
			firstNb = instr[index+1]
		if (secondParamMode == 0):
			secondNb = instr[instr[index+2]]
		else:
			secondNb = instr[index+2]
		res_position = instr[index+3]

		# compute result of instruction
		res = 0
		if opcode == "1":
			res = firstNb + secondNb
			instr[res_position] = res
			index += 4
		elif opcode == "2":
			res = firstNb * secondNb
			instr[res_position] = res
			index += 4
		elif opcode == "3":
			instr[firstNb] = userInput
			index += 2
		elif opcode == "4":
			output = instr[firstNb]
			if (output != 0):
				print output
				break
			index += 2
		else:
			print("error " + opcode)
			break
		


	print("out")