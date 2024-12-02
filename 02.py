import copy
data = "my input".split(",")
data = [int(i) for i in data]
data[1] = 12
data[2] = 2
def intcode(data):
	pc = 0
	while True:
		opcode = data[pc]
		pc+=1
		if opcode == 1:
			tar1 = data[pc]
			tar2 = data[pc+1]
			out = data[pc+2]
			pc+=3
			data[out]=data[tar1]+data[tar2]
		elif opcode == 2:
			tar1 = data[pc]
			tar2 = data[pc+1]
			out = data[pc+2]
			pc+=3
			data[out]=data[tar1]*data[tar2]
		elif opcode == 99:
			return data

print(intcode(copy.deepcopy(data))[0])

for noun in range(99):
	for verb in range(99):
		data[1] = noun
		data[2] = verb
		if intcode(copy.deepcopy(data))[0] == 19690720:
			print(noun*100+verb)
