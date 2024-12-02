data = """my input""".split("\n")

data = [i.split(")") for i in data]

orbits = {}
for i in data:
	orbits[i[1]] = i[0]

total = 0

paths = []

for i in orbits:
	hist = []
	target = i
	while target in orbits:
		hist.append(target)
		total+=1
		target = orbits[target]
	if i=="YOU" or i=="SAN":
		paths.append(hist)

print(total)

for x,i in enumerate(paths[0]):
	if i in paths[1]:
		print(x+paths[1].index(i)-2)
		break
