#On my honor, I have neither given nor received unauthorized aid on this assignment
from sys import argv
"""
Data extraction and preprocessing
instruction -> list
register & datamemory -> dict
key store in register_print & datamemory_print
"""
def read_file_instructions():
	str = ""
	fp = open("./instructions.txt")
	content = fp.readlines()
	content2 = []
	len_con = len(content)
	for i in content:
		if i == content[len_con-1]:
			content2.append(i)
			continue
		i = i[0:-1]
		content2.append(i)
	return content2

def read_file_registers():
	str = ""
	fp = open("./registers.txt")
	content = fp.readlines()
	content2 = []
	len_con = len(content)
	for i in content:
		if i == content[len_con-1]:
			content2.append(i)
			continue
		i = i[0:-1]
		content2.append(i)
	return content2

def read_file_datamemory():
	str = ""
	fp = open("./datamemory.txt")
	content = fp.readlines()
	content2 = []
	len_con = len(content)
	for i in content:
		i = i[0:-1]
		content2.append(i)
	return content2

def process_registers(registers):
	dict_registers = {}
	for i in registers:
		dict_registers[i[1:3]] = i[4:-1]
	return dict_registers

def process_datamemory(datamemory):
	dict_datamemory = {}
	for i in datamemory:
		dict_datamemory[i[1]] = i[3:-1]
	return dict_datamemory

"""
process function
"""
def read():
	pass

def decode(instructions):
	pass



"""
print function
"""
def print(step):
	print("STEP "+ step + ":")
	print()




if __name__ == '__main__':
	registers_print = ["R0","R1","R2","R3","R4","R5","R6","R7"]
	memory_print = ["0","1","2","3","4","5","6","7"]
	instructions = read_file_instructions()
	registers = read_file_registers()
	datamemory = read_file_datamemory()
	dict_registers = {}
	dict_datamemory = {}
	dict_registers = process_registers(registers)
	dict_datamemory = process_datamemory(datamemory)

	#Debug information
	print(dict_registers)
	print(dict_datamemory)
	print(instructions)



	












