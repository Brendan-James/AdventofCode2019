import copy
def processed(rawstring):
	truedata = {}
	for i,v in enumerate(rawstring.split(",")):
		truedata[i] = int(v)
	return truedata

data = processed("my input")

def read(number,mode,data,rb):
	if mode == 0:
		if number not in data:
			return 0
		return data[number]
	elif mode == 1:
		return number
	elif mode == 2:
		if number+rb not in data:
			return 0
		return data[number+rb]
def write(number,mode,data,rb,result):
	if mode == 0:
		data[number] = result
	elif mode == 2:
		data[number+rb] = result
	return data

def intcode(data,inqueue = []):
	pc = 0
	output = []
	ic = 0
	rb = 0
	while pc in data:
		opcode = data[pc] % 100
		mode = data[pc]//100
		modes = []
		for N in range(3):
			modes.append(mode%10)
			mode = mode//10
		pc+=1
		if opcode == 1:
			A = read(data[pc],modes[0],data,rb)
			B = read(data[pc+1],modes[1],data,rb)
			data = write(data[pc+2],modes[2],data,rb,A+B)
			pc+=3
		elif opcode == 2:
			A = read(data[pc],modes[0],data,rb)
			B = read(data[pc+1],modes[1],data,rb)
			data = write(data[pc+2],modes[2],data,rb,A*B)
			pc+=3
		elif opcode == 3:
			if ic<len(inqueue):
				data = write(data[pc],modes[0],data,rb,inqueue[ic])
				ic+=1
			else:
				data = write(data[pc],modes[0],data,rb,int(input("intcode input\n")))
			pc+=1
		elif opcode == 4:
			output.append(read(data[pc],modes[0],data,rb))
			pc+=1
		elif opcode == 5:
			if read(data[pc],modes[0],data,rb)!=0:
				pc = read(data[pc+1],modes[1],data,rb)
			else:
				pc+=2
		elif opcode == 6:
			if read(data[pc],modes[0],data,rb)==0:
				pc = read(data[pc+1],modes[1],data,rb)
			else:
				pc+=2
		elif opcode == 7:
			if read(data[pc],modes[0],data,rb)<read(data[pc+1],modes[1],data,rb):
				data = write(data[pc+2],modes[2],data,rb,1)
			else:
				data = write(data[pc+2],modes[2],data,rb,0)
			pc+=3
		elif opcode == 8:
			if read(data[pc],modes[0],data,rb) == read(data[pc+1],modes[1],data,rb):
				data = write(data[pc+2],modes[2],data,rb,1)
			else:
				data = write(data[pc+2],modes[2],data,rb,0)
			pc+=3
		elif opcode == 9:
			rb += read(data[pc],modes[0],data,rb)
			pc+=1
		elif opcode == 99:
			return output

total = 0
for x in range(50):
	output = ""
	for y in range(50):
		result = intcode(copy.deepcopy(data),[x,y])[0]
		if result == 1:
			output+="#"
		else:
			output+="."
		total += result
	#print(output)

print(total)

x = 11
y = 8
while True:
	opX = x-99
	opY = y+99
	if x>0:
		if intcode(copy.deepcopy(data),[opX,opY])[0] != 0:
			print(opX,y)
			print(opX*10000+y)
			break
	if intcode(copy.deepcopy(data),[x+1,y])[0] == 1:
		x+=1
	else:
		y+=1
