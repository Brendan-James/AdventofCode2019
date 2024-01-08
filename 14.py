import math

data = """1 HKCVW, 2 DFCT => 5 ZJZRN
8 TCPN, 7 XHTJF, 3 DFCT => 8 ZKCXK
1 ZJZRN, 4 NZVL, 1 NJFXK, 7 RHJCQ, 32 MCQS, 1 XFNPT => 5 ZWQX
10 DRWB, 16 JBHKV => 6 TCPN
3 MBFK => 7 DRWB
9 RHJCQ => 6 MBMKZ
1 BVFPF => 2 KRTGD
1 QNXC, 7 BKNQT, 1 XFNPT => 4 VNFJQ
2 TCPN, 1 WFSV => 2 TGJP
35 DFCT => 2 RHJCQ
1 SKBV, 7 CTRH => 8 QGDSV
8 VSRMJ, 1 BVFPF => 4 CTRH
1 WMCD => 3 FPZLF
13 CVJQG, 8 DXBZJ => 9 QBDQ
1 XSRWM => 5 GDJGV
132 ORE => 3 MBFK
2 BQGP => 9 LZKJZ
5 GZLHP => 7 WFSV
2 RXSZS, 10 MBFK, 1 BPNVK => 2 GZLHP
13 BZFH => 8 XSRWM
3 QLSVN => 3 SKBV
8 QBDQ => 4 VSRMJ
1 RXSZS => 9 CVJQG
3 MBFK => 3 BVFPF
7 GZLHP, 4 MBFK, 5 CVJQG => 8 XHTJF
1 GZLHP => 2 DFCT
4 SZDWB, 4 RHJCQ, 1 WMCD => 3 RGZDK
2 BRXLV => 8 DXBZJ
192 ORE => 7 RXSZS
1 PRMR, 6 DFCT => 5 SZDWB
104 ORE => 9 BPNVK
6 VLJWQ, 8 ZKCXK, 6 BKNQT, 26 JRXQ, 7 FPZLF, 6 HKCVW, 18 KRTGD => 4 RBFX
7 XFNPT, 1 GDJGV => 2 HJDB
15 SKBV, 8 DRWB, 12 RXSZS => 3 GHQPH
1 BZFH => 5 GCBR
1 TGJP, 6 SKBV => 1 BZFH
4 KRTGD, 1 ZJHKP, 1 LZKJZ, 1 VNFJQ, 6 QBDQ, 1 PRMR, 1 NJFXK, 1 HJDB => 8 TFQH
10 BVFPF, 1 RGZDK => 8 QNXC
1 XHTJF => 5 JRXQ
3 XKTMK, 4 QGDSV => 3 ZJHKP
2 BZFH => 7 PRMR
1 BPNVK, 1 RXSZS => 5 JBHKV
10 XHTJF => 9 BKNQT
1 JBHKV, 2 XHTJF => 8 QLSVN
24 VNFJQ, 42 TFQH, 39 RBFX, 1 ZWQX, 7 VBHVQ, 26 DRWB, 21 NJFXK => 1 FUEL
26 WBKQ, 14 XHTJF => 5 BQGP
5 WBKQ, 7 MBMKZ => 3 LQGC
6 LQGC => 5 NZVL
13 KRTGD, 5 GHQPH => 9 VLJWQ
117 ORE => 4 BRXLV
3 XKTMK, 1 PRMR => 2 MCQS
3 DRWB, 7 BVFPF, 4 TCPN => 7 NJFXK
10 VHFCR, 13 JZQJ => 5 XKTMK
17 CVJQG, 4 GCBR => 9 HKCVW
22 DFCT, 17 TGJP => 2 WBKQ
2 JZQJ, 12 XFNPT, 1 BQGP => 2 VBHVQ
12 HKCVW => 1 JZQJ
1 XSRWM => 3 WMCD
12 BZFH, 14 SKBV, 1 CTRH => 4 XFNPT
7 ZKCXK => 6 VHFCR""".split("\n")

data2 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX""".split("\n")

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
