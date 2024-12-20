import copy
import heapq
from functools import cmp_to_key

data = """my input""".split("\n")

data = [list(i) for i in data]

"""
floodfill = [(0,0)]

while len(floodfill)>0:
	current = floodfill.pop(0)
	if not (0<=current[0]<len(data) and 0<=current[1]<len(data[0])):
		continue
	if data[current[0]][current[1]] != "#":
		continue
	data[current[0]][current[1]] = "*"
	floodfill.append((current[0]-1,current[1]))
	floodfill.append((current[0]+1,current[1]))
	floodfill.append((current[0],current[1]-1))
	floodfill.append((current[0],current[1]+1))

for i in data:
	print("".join(i))
"""

# since the above code checks that all walls are connected we can ensure there are no meaningful loops

POI = {}

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == "#" or data[y][x] == ".":
			continue
		if data[y][x] == "@":
			start = (x,y)
			continue
		if data[y][x].upper() == data[y][x]:
			continue
		POI[data[y][x]] = (x,y)

#print(POI,start)

def navigate(start, end):
	global data
	pathways = [(start[0],start[1],{},0)]
	visited = {}
	while len(pathways)>0:
		current = pathways.pop(0)
		target = data[current[1]][current[0]]
		if target == "#":
			continue
		if (current[0],current[1]) in visited:
			continue
		visited[(current[0],current[1])] = True
		trace = copy.deepcopy(current[2])
		steps = current[3]
		if (current[0],current[1]) == end:
			return (trace,steps)
		steps+=1
		if target.upper() == target and target.lower() != target:
			trace[target] = True
		pathways.append((current[0]-1,current[1],trace,steps))
		pathways.append((current[0]+1,current[1],trace,steps))
		pathways.append((current[0],current[1]-1,trace,steps))
		pathways.append((current[0],current[1]+1,trace,steps))
	return False


# part 1

routes = {}

for i in POI:
	routes[("@",i)] = navigate(start,POI[i])
	for j in POI:
		if j <= i:
			continue
		routes[(i,j)] = navigate(POI[i],POI[j])

keys =[False]*len(POI)

pathways = [(0,"@",keys)]
heapq.heapify(pathways)
best = 999999999999999

done = {}

while len(pathways)>0:
	#input(pathways)
	steps,curpos,keys = heapq.heappop(pathways)
	if curpos+str(keys) in done:
		continue
	done[curpos+str(keys)] = True
	if all(keys):
		print(steps)
		break
	for i in routes:
		if curpos not in i:
			continue
		if i[0] == curpos:
			otherpos = i[1]
		else:
			otherpos = i[0]
		if otherpos == "@":
			continue
		if keys[ord(otherpos)-97]:
			continue
		for j in routes[i][0]:
			if not keys[ord(j.lower())-97]:
				break
		else:
			newkeys = copy.deepcopy(keys)
			newkeys[ord(otherpos)-97] = True
			newsteps = steps+routes[i][1]
			heapq.heappush(pathways,(newsteps,otherpos,newkeys))



# part 2

data = """my input with the center thing changed out""".split("\n")

data = [list(i) for i in data]

starts = {}

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] in "1234":
			starts[data[y][x]] = (x,y)
			continue

#print(starts)

routes = {}

for i in POI:
	for j in starts:
		result = navigate(starts[j],POI[i])
		if result:
			routes[(j,i)] = result
	for j in POI:
		if j <= i:
			continue
		result = navigate(POI[i],POI[j])
		if result:
			routes[(i,j)] = result

alphabet = "abcdefghijklmnopqrstuvwxyz"

keys =[False]*len(POI)

pathways = [(0,["1","2","3","4"],keys)]
heapq.heapify(pathways)
best = 999999999999999

done = {}

while len(pathways)>0:
	#input(pathways)
	steps,current,keys = heapq.heappop(pathways)
	if str(current)+str(keys) in done:
		continue
	done[str(current)+str(keys)] = True
	if all(keys):
		print(steps)
		break
	for which,curpos in enumerate(current):
		for i in routes:
			if curpos not in i:
				continue
			if i[0] == curpos:
				otherpos = i[1]
			else:
				otherpos = i[0]
			if otherpos in "1234":
				continue
			if keys[ord(otherpos)-97]:
				continue
			for j in routes[i][0]:
				if not keys[ord(j.lower())-97]:
					break
			else:
				newcurr = copy.deepcopy(current)
				newcurr[which] = otherpos
				newkeys = copy.deepcopy(keys)
				newkeys[ord(otherpos)-97] = True
				newsteps = steps+routes[i][1]
				heapq.heappush(pathways,(newsteps,newcurr,newkeys))

