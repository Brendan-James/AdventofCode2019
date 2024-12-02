data = """my input""".split("\n")


data = [list(i) for i in data]
portals = {}

def check(target,x,y):
	if not 0<=x<len(target[0]):
		return " "
	if not 0<=y<len(target):
		return " "
	return target[y][x]

for y in range(len(data)):
	for x in range(len(data[0])):
		side = 5<x<len(data[0])-5 and 5<y<len(data)-5
		if data[y][x] != "#" and data[y][x] != "." and data[y][x] != " ":
			letter1 = data[y][x]
			if check(data,x,y+1) != "#" and check(data,x,y+1) != "." and check(data,x,y+1) != " ":
				letter2 = data[y+1][x]
				if check(data,x,y+2) == ".":
					portals[(x,y+2)] = (letter1+letter2,side)
				else:
					portals[(x,y-1)] = (letter1+letter2,side)
			if check(data,x+1,y) != "#" and check(data,x+1,y) != "." and check(data,x+1,y) != " ":
				letter2 = data[y][x+1]
				if check(data,x+2,y) == ".":
					portals[(x+2,y)] = (letter1+letter2,side)
				else:
					portals[(x-1,y)] = (letter1+letter2,side)

print(portals)

for i in portals:
	if portals[i][0] == "AA":
		positions = [i]
steps = 0
visited = {}
while True:
	newpositions = []
	for i in positions:
		if check(data,i[0],i[1]) != ".":
			continue
		if i in visited:
			continue
		visited[i] = True
		newpositions.append((i[0]-1,i[1]))
		newpositions.append((i[0]+1,i[1]))
		newpositions.append((i[0],i[1]-1))
		newpositions.append((i[0],i[1]+1))
		if i in portals:
			if portals[i][0] == "ZZ":
				print(steps)
				break
			if portals[i][0] == "AA":
				continue
			for j in portals:
				if j==i:
					continue
				if portals[i][0] == portals[j][0]:
					newpositions.append(j)
	else:
		positions = newpositions
		steps += 1
		continue
	break

for i in portals:
	if portals[i][0] == "AA":
		positions = [(i,0)]
steps = 0
visited = {}
while True:
	newpositions = []
	for i,layer in positions:
		if layer<0:
			continue
		if check(data,i[0],i[1]) != ".":
			continue
		if (i,layer) in visited:
			continue
		visited[(i,layer)] = True
		newpositions.append(((i[0]-1,i[1]),layer))
		newpositions.append(((i[0]+1,i[1]),layer))
		newpositions.append(((i[0],i[1]-1),layer))
		newpositions.append(((i[0],i[1]+1),layer))
		if i in portals:
			if portals[i][0] == "ZZ" and layer == 0:
				print(steps)
				break
			if portals[i][0] == "AA":
				continue
			for j in portals:
				if j==i:
					continue
				if portals[i][0] == portals[j][0]:
					if portals[i][1]:
						newpositions.append((j,layer+1))
					else:
						newpositions.append((j,layer-1))
	else:
		positions = newpositions
		steps += 1
		continue
	break
