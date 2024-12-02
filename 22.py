import copy
data = """my input""".split("\n")

def parse(data,n):
	deck = list(range(n))
	for i in data:
		if i == "deal into new stack":
			deck.reverse()
		elif i[:4] == "cut ":
			deck = deck[int(i[4:]):]+deck[:int(i[4:])]
		elif i[:20] == "deal with increment ":
			newdeck = [0]*len(deck)
			target = 0
			for j in deck:
				newdeck[target] = j
				target+=int(i[20:])
				target%=len(deck)
			deck = newdeck
	return deck



print(parse(data,10007).index(2019))



# WELCOME TO THE THEORY CORNER

# CUT X DEAL Y REVERSE Y/N -> cut N = CUT X+/-(inv(Y)*N) DEAL Y REVERSE Y/N
# X 2 Y + 3 = X-7 2 Y @ 11
# X 2 N + 3 = X+7 2 N @ 11
# X 2 N + 4 = X+2 2 N @ 11
# X 3 N + 2 = X+8 3 N @ 11
# X 3 N + 2 = X+5 3 N @ 13

# X Y N + Y = X+1 Y N

# CUT X DEAL Y REVERSE N -> deal N = CUT X DEAL Y*N REVERSE N
# CUT X DEAL Y REVERSE Y -> deal N = CUT X+? DEAL Y*N REVERSE Y

# CUT X DEAL Y REVERSE Y/N -> Reverse = CUT X DEAL Y REVERSE N/Y


# deal with X -> deal with Y = deal with X*Y
# cut X -> cut Y = cut X+Y
# cut X -> reverse = reverse -> cut -X
# cut X -> deal with Y = deal with Y -> cut X*Y (% N)
# deal with X -> cut X-1  -> reverse = reverse -> deal with X
# cut inv(X)*(X-1) -> deal with X -> reverse = reverse -> deal with X
# cut A -> deal with B -> reverse -> deal with X = cut A -> deal with B -> deal with X -> cut X-1  -> reverse

# 3*2 = +2 6 @ 13
# 2*3 = +4 6 @ 13
# 3*2 = +0?? 6 @ 11
# 2*3 = +7 6 @ 11

# cut A -> deal with B -> reverse -> deal with X = cut A -> deal with B -> deal with X -> cut X-1  -> reverse
# = cut A -> deal with B*X -> cut X-1  -> reverse

def cuts(CDS,c):
	cut,deal,size = CDS
	return ((cut+pow(deal,-1,size)*c)%size,deal,size)
def deals(CDS,d):
	cut,deal,size = CDS
	return (cut,deal*d%size,size)

def actualize(CDS):
	cut,deal,size = CDS
	output = f"""cut {cut}\ndeal with increment {deal}"""
	return output.split("\n")

bigsize = 119315717514047


CDS = (0,1,bigsize)

for i in data:
	if i == "deal into new stack":
		CDS = deals(CDS,-1)
		CDS = cuts(CDS,1)
	elif i[:4] == "cut ":
		CDS = cuts(CDS,int(i[4:]))
	elif i[:20] == "deal with increment ":
		CDS = deals(CDS,int(i[20:]))

target = str(bin(101741582076661))[2:]
mask = []

for i in reversed(target):
	mask.append(i=="1")

powers = []

def addup(CDS1,CDS2):
	return deals(cuts(CDS1,CDS2[0]),CDS2[1])

for i in mask:
	powers.append(copy.deepcopy(CDS))
	CDS = addup(CDS,CDS)

CDS = (0,1,119315717514047)
for i,v in enumerate(mask):
	if v:
		CDS = addup(CDS,powers[i])

inversedeal = pow(CDS[1],-1,bigsize)
normalcut = CDS[0]
print((2020*inversedeal+normalcut)%bigsize)
