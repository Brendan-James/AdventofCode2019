wire1 = "my input 1".split(",")
wire2 = "my input 2".split(",")


corners1 = [(0,0)]
directions = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
for i in wire1:
	direction = directions[i[0]]
	distance = int(i[1:])
	prev = corners1[-1]
	corners1.append((prev[0]+direction[0]*distance,prev[1]+direction[1]*distance))

corners2 = [(0,0)]
directions = {"R":(1,0),"L":(-1,0),"U":(0,1),"D":(0,-1)}
for i in wire2:
	direction = directions[i[0]]
	distance = int(i[1:])
	prev = corners2[-1]
	corners2.append((prev[0]+direction[0]*distance,prev[1]+direction[1]*distance))

intersections = []

def cross(a1,a2,b):
	return min(a1,a2)<=b<=max(a1,a2)

for i in range(len(corners1)-1):
	for j in range(len(corners2)-1):
		spanA = (corners1[i],corners1[i+1])
		spanB = (corners2[j],corners2[j+1])
		if spanA[0][0] == spanA[1][0] and spanB[0][1] == spanB[1][1]:
			if cross(spanA[0][1],spanA[1][1],spanB[0][1]) and cross(spanB[0][0],spanB[1][0],spanA[0][0]):
				intersections.append((spanA[0][0],spanB[1][1]))
		if spanB[0][0] == spanB[1][0] and spanA[0][1] == spanA[1][1]:
			if cross(spanB[0][1],spanB[1][1],spanA[0][1]) and cross(spanA[0][0],spanA[1][0],spanB[0][0]):
				intersections.append((spanB[0][0],spanA[1][1]))
total = 99999999

for i in intersections:
	total = min(abs(i[0])+abs(i[1]),total)

print(total)

scores = [0 for i in intersections]
visited = [False for i in intersections]

current = (0,0)
steps = 0
for i in wire1:
	direction = directions[i[0]]
	for j in range(int(i[1:])):
		steps+=1
		current = (current[0]+direction[0],current[1]+direction[1])
		for k in range(len(intersections)):
			if visited[k]:
				continue
			if intersections[k] == current:
				visited[k] = True
				scores[k]+=steps

visited = [False for i in intersections]

current = (0,0)
steps = 0
for i in wire2:
	direction = directions[i[0]]
	for j in range(int(i[1:])):
		steps+=1
		current = (current[0]+direction[0],current[1]+direction[1])
		for k in range(len(intersections)):
			if visited[k]:
				continue
			if intersections[k] == current:
				visited[k] = True
				scores[k]+=steps

print(min(scores))
