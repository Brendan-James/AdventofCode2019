# day 13 is great

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

result = intcode(data)

print(result)

screen = {}

for i in range(len(result)//3):
	start = i*3
	screen[(result[start],result[start+1])] = result[start+2]

total = 0
for i in screen:
	if screen[i]==2:
		total+=1

print(total)

data = "my input but the 1 is changes to a 2".split(",")

truedata = {}
for i,v in enumerate(data):
	truedata[i] = int(v)

data = truedata

def render(result):
	for i in range(len(result)//3):
		start = i*3
		screen[(result[start],result[start+1])] = result[start+2]
	ball = 0
	paddle = 0
	tiles = [" ","#","X","=","O"]
	frame = ""
	for y in range(24):
		for x in range(41):
			frame+=tiles[screen[(x,y)]]
			if screen[(x,y)] == 3:
				paddle = x
			if screen[(x,y)] == 4:
				ball = x
		frame+="\n"
	frame+="SCORE:" + str(screen[(-1,0)])
	print(frame)
	if ball==paddle:
		return 0
	if ball>paddle:
		return 1
	return -1

def play(data,inqueue = []):
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
				print("AI SUGGESTION:",render(output))
				output = []
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

def autoplay(data,inqueue = []):
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
				data = write(data[pc],modes[0],data,rb,render(output))
				output = []
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

render(autoplay(data))
