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
	outstring = ""
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
			if output[-1]<300:
				outstring+=chr(output[-1])
			if len(output)>=2:
				if output[-1] == output[-2] == 10:
					print(outstring)
					outstring = ""
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

output = intcode(data)

grid = []
newline = []

for i in output:
	if i == 10:
		grid.append(newline)
		newline = []
	else:
		newline.append(chr(i))
grid = grid[:-1]

total = 0

for x in range(1,len(grid[0])-1):
	for y in range(1,len(grid)-1):
		if grid[y][x] == ".":
			continue
		if grid[y-1][x] == ".":
			continue
		if grid[y+1][x] == ".":
			continue
		if grid[y][x-1] == ".":
			continue
		if grid[y][x+1] == ".":
			continue
		total+=x*y

print(total)
data = processed("my input but the 1 is changed to a 2")


main = "A,A,B,C,B,A,C,B,C,A"
A = "L,6,R,12,L,6,L,8,L,8"
B = "L,6,R,12,R,8,L,8"
C = "L,4,L,4,L,6"

#should do a good job handling the continous video feed V flag being set to y
full = [ord(i) for i in main+"\n"+A+"\n"+B+"\n"+C+"\n"+"n"+"\n"]

print(intcode(data,full)[-1])
