data = "my input".split(",")
truedata = {}
for i,v in enumerate(data):
	truedata[i] = int(v)

data = truedata

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

def intcode(data):
	global panels
	pc = 0
	output = []
	rb = 0
	x = 0
	y = 0
	facing = (0,-1)
	parity = 0
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
			"""if ic<len(inqueue):
				data = write(data[pc],modes[0],data,rb,inqueue[ic])
				ic+=1
			else:
				data = write(data[pc],modes[0],data,rb,int(input("intcode input")))"""
			if (x,y) in panels:
				data = write(data[pc],modes[0],data,rb,panels[(x,y)])
			else:
				data = write(data[pc],modes[0],data,rb,0)
			pc+=1
		elif opcode == 4:
			result = read(data[pc],modes[0],data,rb)
			if parity == 0:
				panels[(x,y)] = result
				parity = 1
			else:
				facing = (-facing[1],facing[0])
				if result == 0:
					facing = (-facing[0],-facing[1])
				x+=facing[0]
				y+=facing[1]
				parity = 0
			#output.append(read(data[pc],modes[0],data,rb))
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
			return panels
panels = {}
print(len(intcode(data)))

panels = {(0,0):1}
result = intcode(data)

for y in range(6):
	output = ""
	for x in range(40):
		if (x,y) in result:
			if result[(x,y)] == 1:
				output+="#"
			else:
				output+=" "
		else:
			output+=" "
	print(output)
