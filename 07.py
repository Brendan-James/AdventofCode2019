import itertools

data = "3,8,1001,8,10,8,105,1,0,0,21,34,43,64,85,98,179,260,341,422,99999,3,9,1001,9,3,9,102,3,9,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,1001,9,3,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,102,3,9,9,101,4,9,9,102,3,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99".split(",")

data = [int(i) for i in data]

def read(number,mode,data):
	if mode == 0:
		return data[number]
	elif mode == 1:
		return number

def intcode(data,inqueue = []):
	pc = 0
	output = []
	ic = 0
	while pc<len(data):
		opcode = data[pc] % 100
		mode = data[pc]//100
		modes = []
		for N in range(3):
			modes.append(mode%10)
			mode = mode//10
		pc+=1
		if opcode == 1:
			A = read(data[pc],modes[0],data)
			B = read(data[pc+1],modes[1],data)
			data[data[pc+2]]=A+B
			pc+=3
		elif opcode == 2:
			A = read(data[pc],modes[0],data)
			B = read(data[pc+1],modes[1],data)
			data[data[pc+2]]=A*B
			pc+=3
		elif opcode == 3:
			if ic<len(inqueue):
				data[data[pc]] = inqueue[ic]
				ic+=1
			else:
				data[data[pc]] = int(input("intcode input\n"))
			pc+=1
		elif opcode == 4:
			output.append(read(data[pc],modes[0],data))
			pc+=1
		elif opcode == 5:
			if read(data[pc],modes[0],data)!=0:
				pc = read(data[pc+1],modes[1],data)
			else:
				pc+=2
		elif opcode == 6:
			if read(data[pc],modes[0],data)==0:
				pc = read(data[pc+1],modes[1],data)
			else:
				pc+=2
		elif opcode == 7:
			if read(data[pc],modes[0],data)<read(data[pc+1],modes[1],data):
				data[data[pc+2]] = 1
			else:
				data[data[pc+2]] = 0
			pc+=3
		elif opcode == 8:
			if read(data[pc],modes[0],data) == read(data[pc+1],modes[1],data):
				data[data[pc+2]] = 1
			else:
				data[data[pc+2]] = 0
			pc+=3
		elif opcode == 99:
			return output

total = 0

for i in itertools.permutations(range(5)):
	current = 0
	for j in i:
		current = intcode(data,[j,current])[0]
	total = max(total,current)

print(total)

# hopefully the progressive inputs don't show up again
def intcodespecial(data,steps,inqueue = []):
	pc = 0
	output = []
	ic = 0
	while pc<len(data):
		opcode = data[pc] % 100
		mode = data[pc]//100
		modes = []
		for N in range(3):
			modes.append(mode%10)
			mode = mode//10
		pc+=1
		if opcode == 1:
			A = read(data[pc],modes[0],data)
			B = read(data[pc+1],modes[1],data)
			data[data[pc+2]]=A+B
			pc+=3
		elif opcode == 2:
			A = read(data[pc],modes[0],data)
			B = read(data[pc+1],modes[1],data)
			data[data[pc+2]]=A*B
			pc+=3
		elif opcode == 3:
			if ic<len(inqueue):
				data[data[pc]] = inqueue[ic]
				ic+=1
			else:
				return output,False
			pc+=1
		elif opcode == 4:
			output.append(read(data[pc],modes[0],data))
			pc+=1
			steps-=1
			if steps==0:
				return output,False
		elif opcode == 5:
			if read(data[pc],modes[0],data)!=0:
				pc = read(data[pc+1],modes[1],data)
			else:
				pc+=2
		elif opcode == 6:
			if read(data[pc],modes[0],data)==0:
				pc = read(data[pc+1],modes[1],data)
			else:
				pc+=2
		elif opcode == 7:
			if read(data[pc],modes[0],data)<read(data[pc+1],modes[1],data):
				data[data[pc+2]] = 1
			else:
				data[data[pc+2]] = 0
			pc+=3
		elif opcode == 8:
			if read(data[pc],modes[0],data) == read(data[pc+1],modes[1],data):
				data[data[pc+2]] = 1
			else:
				data[data[pc+2]] = 0
			pc+=3
		elif opcode == 99:
			return output,True

total = 0
for i in itertools.permutations([i+5 for i in range(5)]):
	current = [[j] for j in i]
	current[0].append(0)
	flag = True
	steps = 2
	while flag:
		for j in range(5):
			new = intcodespecial(data,steps,current[j])
			current[(j+1)%5].append(new[0][-1])
			if new[1]:
				flag = False
			steps+=1
	total = max(total,current[0][-1])
print(total)
