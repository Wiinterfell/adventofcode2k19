import sys


for i in range (0,99):
	for j in range(0,99):

		with open("input2.txt") as fp:
 			instr_str = fp.readline().split(",")
			instr = list(map(int, instr_str))
	
			instr[1] = i
			instr[2] = j

	
			index = 0
			while(instr[index] != 99):
				firstNb = instr[instr[index+1]]
				secondNb = instr[instr[index+2]]
				res = 0
				if instr[index] == 1:
					res = firstNb + secondNb
				else:
					res = firstNb * secondNb
				res_position = instr[index+3]
				instr[res_position] = res
				index += 4

			if (instr[0] == 19690720):
				print(str(100*i+j))