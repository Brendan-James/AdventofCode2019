datamin = "my input 1"
datamax = "my input 2"

total = 0

for A in range(0,10):
	for B in range(A,10):
		for C in range(B,10):
			for D in range(C,10):
				for E in range(D,10):
					for F in range(E,10):
						if A!=B and B!=C and C!=D and D!=E and E!=F:
							continue
						num = F+E*10+D*100+C*1000+B*10000+A*100000
						if datamin<=num<=datamax:
							total+=1


print(total)
total = 0

for A in range(0,10):
	for B in range(A,10):
		for C in range(B,10):
			for D in range(C,10):
				for E in range(D,10):
					for F in range(E,10):
						num = F+E*10+D*100+C*1000+B*10000+A*100000
						if datamin<=num<=datamax:
							if A==B!=C or A!=B==C!=D or B!=C==D!=E or C!=D==E!=F or D!=E==F:
								total+=1

print(total)
