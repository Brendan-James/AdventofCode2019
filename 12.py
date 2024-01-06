import math

data = [[[5,13,-3],[0,0,0]],[[18,-7,13],[0,0,0]],[[16,3,4],[0,0,0]],[[0,8,8],[0,0,0]]]
"""
<x=5, y=13, z=-3>
<x=18, y=-7, z=13>
<x=16, y=3, z=4>
<x=0, y=8, z=8>
"""

data2 = [[[-8,-10,0],[0,0,0]],[[5,5,10],[0,0,0]],[[2,-7,3],[0,0,0]],[[9,-8,-3],[0,0,0]]]
"""
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""

data3 = [[[-1,0,2],[0,0,0]],[[2,-10,-7],[0,0,0]],[[4,-8,8],[0,0,0]],[[3,5,-1],[0,0,0]]]
"""
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""

def sign(n):
	if n>0:
		return 1
	if n==0:
		return 0
	return -1

def step(data):
	for i in range(len(data)):
		for j in range(i+1,len(data)):
			for axis in range(3):
				data[i][1][axis]+=sign(data[j][0][axis]-data[i][0][axis])
				data[j][1][axis]+=sign(data[i][0][axis]-data[j][0][axis])
	for i in range(len(data)):
		for axis in range(3):
			data[i][0][axis]+=data[i][1][axis]
	return data

for steps in range(1000):
	data = step(data)

total = 0

for i in data:
	subsums = [0,0]
	for n,j in enumerate(i):
		for k in j:
			subsums[n]+=abs(k)
	total+=subsums[0]*subsums[1]

print(total)

prevx = []
prevy = []
prevz = []


data = [[[5,13,-3],[0,0,0]],[[18,-7,13],[0,0,0]],[[16,3,4],[0,0,0]],[[0,8,8],[0,0,0]]]

todo = [True,True,True]
results = [[],[],[]]

while any(todo):
	justx = []
	justy = []
	justz = []
	for i in data:
		for j in i:
			justx.append(j[0])
			justy.append(j[1])
			justz.append(j[2])
	justx = str(justx)
	justy = str(justy)
	juztz = str(justz)
	if todo[0]:
		if justx in prevx:
			results[0] = [prevx.index(justx),len(prevx)]
			todo[0] = False
		else:
			prevx.append(justx)
	if todo[1]:
		if justy in prevy:
			results[1] = [prevy.index(justy),len(prevy)]
			todo[1] = False
		else:
			prevy.append(justy)
	if todo[2]:
		if justz in prevz:
			results[2] = [prevz.index(justz),len(prevz)]
			todo[2] = False
		else:
			prevz.append(justz)
	data = step(data)

print(steps)
print(results)

total = 1

for x,i in results:
	total = math.lcm(total,i)

print(total)
