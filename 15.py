import copy

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

def visualize(maps,curx,cury):
	xfront = 0
	yfront = 0
	xend = 0
	yend = 0
	for i in maps:
		xfront = min(xfront,i[0])
		xend = max(xend,i[0])
		yfront = min(yfront,i[1])
		yend = max(yend,i[1])
	output = ""
	for y in range(yfront,yend+1):
		for x in range(xfront, xend+1):
			if x == curx and y== cury:
				output+="*"
			elif (x,y) in maps:
				output += maps[(x,y)]
			else:
				output += " "
		output+="\n"
	return output

def navigate(maps,x,y,tarx,tary):
	dirs = [(0,-1),(0,1),(1,0),(-1,0)]
	visited = {}
	todo = [(x,y,[])]
	while len(todo)>0:
		newdo = []
		for curx,cury,trail in todo:
			visited[(curx,cury)] = True
			for j,v in enumerate(dirs):
				newtrail = copy.deepcopy(trail)
				newtrail.append(j+1)
				newx = v[0] + curx
				newy = v[1] + cury
				if newx == tarx and newy == tary:
					return newtrail
				if (newx,newy) in visited:
					continue
				if maps[newx,newy] == "?" or maps[newx,newy] == "#":
					continue
				newdo.append((newx,newy,newtrail))
		todo = newdo
	print("disaster")
	return []

def intcode(data,inqueue = []):
	pc = 0
	output = 0
	ic = 0
	rb = 0
	x = 0
	y = 0
	dirs = [(0,-1),(0,1),(1,0),(-1,0)]
	prevdir = (0,0)
	maps = {(1,0):"?",(-1,0):"?",(0,1):"?",(0,-1):"?",(0,0):"X"}
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
				nexter = inqueue[ic]
				ic+=1
			else:
				nexter = int(input("intcode input\n"))
			data = write(data[pc],modes[0],data,rb,nexter)
			prevdir = dirs[nexter-1]
			pc+=1
		elif opcode == 4:
			output = read(data[pc],modes[0],data,rb)
			if output == 0:
				maps[(x+prevdir[0],y+prevdir[1])] = "#"
			elif output == 1:
				x += prevdir[0]
				y += prevdir[1]
				if (x,y) not in maps:
					maps[(x,y)] = "."
				elif maps[(x,y)] == "?":
					maps[(x,y)] = "."
			else:
				x += prevdir[0]
				y += prevdir[1]
				maps[(x,y)] = "!"
			for i in dirs:
				tempx = x+i[0]
				tempy = y+i[1]
				if (tempx,tempy) not in maps:
					maps[tempx,tempy] = "?"
			if ic == len(inqueue):
				best = (0,0)
				bestdist = 999999
				for i in maps:
					if maps[i] == "?":
						if abs(i[0]-x)+abs(i[1]-y) < bestdist:
							best = i
							bestdist = abs(i[0]-x)+abs(i[1]-y)
				if bestdist == 999999:
					return maps
				inqueue = navigate(maps,x,y,best[0],best[1])
				ic = 0
			print(visualize(maps,x,y))
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
			return maps

result = intcode(data,[1])
print(visualize(result,0,0))
longest = 0
for i in result:
	if result[i] == "!":
		print(len(navigate(result,0,0,i[0],i[1])))
		dirs = [(0,-1),(0,1),(1,0),(-1,0)]
		steps = 0
		todo = [(i[0],i[1])]
		visited = {}
		while len(todo)>0:
			steps+=1
			newdo=[]
			for i in todo:
				visited[i] = True
				for j in dirs:
					newx = i[0]+j[0]
					newy = i[1]+j[1]
					if (newx,newy) in visited:
						continue
					if result[(newx,newy)] == "#":
						continue
					newdo.append((newx,newy))
			todo = newdo
		print(steps-1)
		break
