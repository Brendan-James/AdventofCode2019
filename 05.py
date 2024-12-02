data = "my input".split(",")
data = [int(i) for i in data]

def read(number,mode,data):
	if mode == 0:
		return data[number]
	elif mode == 1:
		return number

def intcode(data):
	pc = 0
	output = []
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
			return data,output

print(intcode(data)[1])
