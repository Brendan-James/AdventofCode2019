data = [int(i) for i in "my input"]
data2 = [int(i) for i in "12345678"]
"""
base = [0, 1, 0, -1]

for step in range(100):
	new = []
	for i in range(len(data)):
		count = 0
		spot = 0
		total = 0
		for j in data:
			count+=1
			if count>=i+1:
				count=0
				spot+=1
				spot%=4
			total+=base[spot]*j
		new.append(abs(total)%10)
	data = new

print("".join([str(i) for i in data[:8]]))
"""

# not a fan of this version of oops! spot the trick
# you can tell because it took me 2 months to actually focus enough to finish this one

offset = 5970443

memorize = {}
for step in range(101):
	memorize[(step,6500000)] = 0
for step in range(101):
	for pos in reversed(range(offset,6500000)):
		if step == 0:
			memorize[(step,pos)] = data[pos%len(data)]
		else:
			memorize[(step,pos)] = (memorize[(step-1,pos)]+memorize[(step,pos+1)])%10

output = ""

for i in range(8):
	output+=str(memorize[(100,i+offset)])

print(output)
