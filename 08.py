data = "my input"

data = [int(i) for i in data]

indent = 0
layers = []

while indent<len(data)-1:
	layers.append([])
	for y in range(6):
		for x in range(25):
			layers[-1].append(data[indent])
			indent+=1

best = 9999999
bestie = 0

for i in layers:
	counts = [0,0,0]
	for j in i:
		counts[j]+=1
	if counts[0]<best:
		best = counts[0]
		bestie = counts[1]*counts[2]

print(bestie)

for y in range(6):
	output = ""
	for x in range(25):
		indent = y*25+x
		for l in layers:
			if l[indent] == 2:
				continue
			if l[indent] == 0:
				output+="."
				break
			if l[indent] == 1:
				output+="#"
				break
	print(output)
