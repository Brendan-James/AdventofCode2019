import copy
data = """.##.#
###..
#...#
##.#.
.###.""".split("\n")

data = [list(i) for i in data]

def read(data,x,y):
	if not 0<=x<len(data[0]):
		return " "
	if not 0<=y<len(data):
		return " "
	return data[y][x]

def adjcheck(data,x,y):
	count = 0
	if read(data,x-1,y) == "#":
		count+=1
	if read(data,x+1,y) == "#":
		count+=1
	if read(data,x,y-1) == "#":
		count+=1
	if read(data,x,y+1) == "#":
		count+=1
	return count

prev = {}

while str(data) not in prev:
	prev[str(data)] = True
	new = []
	for y in range(5):
		newln = []
		for x in range(5):
			count = adjcheck(data,x,y)
			if data[y][x] == "#" and count == 1 or data[y][x] == "." and 0<count<3:
				newln.append("#")
			else:
				newln.append(".")
		new.append(newln)
	data = new


total = 0
for x in range(5):
	for y in range(5):
		if data[y][x]=="#":
			total+=2**(x+y*5)

print(total)

data = """.##.#
###..
#.?.#
##.#.
.###.""".split("\n")

empty = """.....
.....
..?..
.....
.....""".split("\n")

data = [list(i) for i in data]
empty =[list(i) for i in empty]
data = {-1:copy.deepcopy(empty),0:data,1:copy.deepcopy(empty)}

def read2(data,x,y,layer,direction):
	if layer not in data:
		return 0
	if x<0:
		return read2(data,1,2,layer-1,direction)
	if x>4:
		return read2(data,3,2,layer-1,direction)
	if y<0:
		return read2(data,2,1,layer-1,direction)
	if y>4:
		return read2(data,2,3,layer-1,direction)
	if data[layer][y][x] == "?":
		count = 0
		for i in range(5):
			if direction[0] == 0:
				if direction[1] == 1:
					count+=read2(data,i,0,layer+1,direction)
				else:
					count+=read2(data,i,4,layer+1,direction)
			else:
				if direction[0] == 1:
					count+=read2(data,0,i,layer+1,direction)
				else:
					count+=read2(data,4,i,layer+1,direction)
		return count
	return data[layer][y][x]=="#"

def adjcheck2(data,x,y,layer):
	count = 0
	count+=read2(data,x-1,y,layer,(-1,0))
	count+=read2(data,x+1,y,layer,(1,0))
	count+=read2(data,x,y-1,layer,(0,-1))
	count+=read2(data,x,y+1,layer,(0,1))
	return count


for i in range(200):
	new = {}
	for layer in data:
		for row in data[layer]:
			if "#" in row:
				if layer-1 not in new:
					new[layer-1] = copy.deepcopy(empty)
				if layer+1 not in new:
					new[layer+1] = copy.deepcopy(empty)
		newlayer = []
		for y in range(5):
			newln = []
			for x in range(5):
				if x==y==2:
					newln.append("?")
					continue
				count = adjcheck2(data,x,y,layer)
				if data[layer][y][x] == "#" and count == 1 or data[layer][y][x] == "." and 0<count<3:
					newln.append("#")
				else:
					newln.append(".")
			newlayer.append(newln)
		new[layer] = newlayer
	data = new

count = 0
for layer in data:
	for y in range(5):
		for x in range(5):
			if data[layer][y][x] == "#":
				count+=1

print(count)
