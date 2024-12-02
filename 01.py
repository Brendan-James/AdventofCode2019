data = """my input""".split("\n")

total = 0
for i in data:
	total+=int(i)//3-2


print(total)

total = 0

for i in data:
	current = int(i)//3-2
	while current>=0:
		total+=current
		current = current//3-2

print(total)
