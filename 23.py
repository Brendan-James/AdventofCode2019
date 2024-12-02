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

def step(data,inqueue,pc,output,ic,rb,idle):
	trueoutput = []
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
			idle = False
		else:
			data = write(data[pc],modes[0],data,rb,-1)
			idle = True
		pc+=1
	elif opcode == 4:
		output.append(read(data[pc],modes[0],data,rb))
		if len(output) % 3 == 0:
			trueoutput = output[-3:]
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
	return (data,inqueue,pc,output,ic,rb,trueoutput,idle)

states = {}
for i in range(50):
	states[i] = (copy.deepcopy(data),[i],0,[],0,0,False)

previous = "NaN"

while True:
	idles = []
	for i in range(50):
		data,inqueue,pc,output,ic,rb,idle = states[i]
		data,inqueue,pc,output,ic,rb,trueoutput,idle = step(data,inqueue,pc,output,ic,rb,idle)
		if len(trueoutput)==3:
			#print(i,trueoutput)
			if trueoutput[0] not in states:
				states[trueoutput[0]] = [trueoutput[0],[]]
				if trueoutput[0] == 255:
					print(trueoutput[2])
			states[trueoutput[0]][1].append(trueoutput[1])
			states[trueoutput[0]][1].append(trueoutput[2])
			if 0<=trueoutput[0]<50:
				T = states[trueoutput[0]]
				states[trueoutput[0]] = (T[0],T[1],T[2],T[3],T[4],T[5],False)
		states[i] = (data,inqueue,pc,output,ic,rb,idle)
	if all([states[i][6] for i in range(50)]) and 255 in states:
		#print("all idle, firing")
		#print(states[255][1][-2:])
		if states[255][1][-1] == previous:
			print("final")
			print(previous)
			break
		previous = states[255][1][-1]
		states[0][1].append(states[255][1][-2])
		states[0][1].append(states[255][1][-1])
		T = states[0]
		states[0] = (T[0],T[1],T[2],T[3],T[4],T[5],False)
