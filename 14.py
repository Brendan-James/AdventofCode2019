import math

data = """my input""".split("\n")

data2 = """small scale example""".split("\n")

data = [[[[int(k.split(" ")[0]),k.split(" ")[1]] for k in j.split(", ")] for j in i.split(" => ")] for i in data]

for i in range(len(data)):
	data[i][1] = data[i][1][0]

leftovers = {"BPNVK":0}
goals = [["FUEL",1]]

result = 0

def acquire(target,quantity):
	global data
	global leftovers
	global goals
	global result
	if target in leftovers:
		if leftovers[target]>=quantity:
			leftovers[target]-=quantity
			return
		quantity-=leftovers[target]
		leftovers[target] = 0

	for i in data:
		if i[1][1] == target:
			num = int(math.ceil(quantity/i[1][0]))
			for j in i[0]:
				if j[1] == "ORE":
					result+=j[0]*num
				else:
					goals.append([j[1],j[0]*num])
			left = (i[1][0]*num)-quantity
			if left!=0:
				if target not in leftovers:
					leftovers[target] = 0
				leftovers[target] += left
			return

while len(goals)>0:
	target,quantity = goals.pop(0)
	acquire(target,quantity)

print(result)

# 1.88 is a handpicked value
guess = int((1000000000000/result) * 1.88)
count = guess
goals = [["FUEL",guess]]
while len(goals)>0:
	target,quantity = goals.pop(0)
	acquire(target,quantity)
print(result)
while result < 1000000000000:
	goals = [["FUEL",1]]
	count+=1
	while len(goals)>0:
		target,quantity = goals.pop(0)
		acquire(target,quantity)

print(count)
