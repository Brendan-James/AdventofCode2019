import copy
data = """deal with increment 33
cut 3627
deal with increment 29
cut 1908
deal with increment 32
deal into new stack
cut 8923
deal with increment 19
cut 8560
deal with increment 73
deal into new stack
deal with increment 30
cut 8832
deal with increment 70
deal into new stack
deal with increment 11
cut -4208
deal with increment 47
deal into new stack
deal with increment 65
cut -5055
deal with increment 66
cut 12
deal with increment 24
cut 3069
deal into new stack
cut -1271
deal with increment 50
cut -7214
deal with increment 72
deal into new stack
cut 67
deal with increment 60
cut -7515
deal with increment 68
deal into new stack
cut -4640
deal with increment 68
cut -9047
deal with increment 53
cut 3616
deal with increment 39
deal into new stack
deal with increment 54
cut -6224
deal with increment 42
deal into new stack
deal with increment 35
deal into new stack
cut -4189
deal with increment 68
deal into new stack
cut 425
deal with increment 28
cut -9932
deal with increment 18
deal into new stack
cut 6404
deal with increment 64
cut -724
deal with increment 33
deal into new stack
cut -8328
deal into new stack
cut 4667
deal with increment 37
cut 3303
deal with increment 13
deal into new stack
deal with increment 56
cut 2288
deal with increment 13
cut -266
deal with increment 65
cut 445
deal with increment 33
cut 2652
deal with increment 57
cut -9924
deal with increment 56
cut 9807
deal into new stack
cut -1485
deal with increment 35
cut -4846
deal with increment 5
cut 7747
deal with increment 44
cut -7428
deal with increment 71
deal into new stack
cut -7677
deal with increment 3
cut -5335
deal with increment 31
cut 7778
deal with increment 5
cut 11
deal into new stack
deal with increment 32""".split("\n")

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
