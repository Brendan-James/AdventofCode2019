import math
from functools import cmp_to_key
data = """.#....#.###.........#..##.###.#.....##...
...........##.......#.#...#...#..#....#..
...#....##..##.......#..........###..#...
....#....####......#..#.#........#.......
...............##..#....#...##..#...#..#.
..#....#....#..#.....#.#......#..#...#...
.....#.#....#.#...##.........#...#.......
#...##.#.#...#.......#....#........#.....
....##........#....#..........#.......#..
..##..........##.....#....#.........#....
...#..##......#..#.#.#...#...............
..#.##.........#...#.#.....#........#....
#.#.#.#......#.#...##...#.........##....#
.#....#..#.....#.#......##.##...#.......#
..#..##.....#..#.........#...##.....#..#.
##.#...#.#.#.#.#.#.........#..#...#.##...
.#.....#......##..#.#..#....#....#####...
........#...##...#.....#.......#....#.#.#
#......#..#..#.#.#....##..#......###.....
............#..#.#.#....#.....##..#......
...#.#.....#..#.......#..#.#............#
.#.#.....#..##.....#..#..............#...
.#.#....##.....#......##..#...#......#...
.......#..........#.###....#.#...##.#....
.....##.#..#.....#.#.#......#...##..#.#..
.#....#...#.#.#.......##.#.........#.#...
##.........#............#.#......#....#..
.#......#.............#.#......#.........
.......#...##........#...##......#....#..
#..#.....#.#...##.#.#......##...#.#..#...
#....##...#.#........#..........##.......
..#.#.....#.....###.#..#.........#......#
......##.#...#.#..#..#.##..............#.
.......##.#..#.#.............#..#.#......
...#....##.##..#..#..#.....#...##.#......
#....#..#.#....#...###...#.#.......#.....
.#..#...#......##.#..#..#........#....#..
..#.##.#...#......###.....#.#........##..
#.##.###.........#...##.....#..#....#.#..
..........#...#..##..#..##....#.........#
..#..#....###..........##..#...#...#..#..""".split("\n")

asteroids = {}

for y in range(len(data)):
	for x in range(len(data[0])):
		if data[y][x] == "#":
			asteroids[(x,y)] = True

laser = (0,0)

best = 0
for i in asteroids:
	count = 0
	for j in asteroids:
		if i==j:
			continue
		dx = abs(i[0]-j[0])
		dy = abs(i[1]-j[1])
		steps = math.gcd(dx,dy)
		dx = j[0]-i[0]
		dy = j[1]-i[1]
		dx = dx//steps
		dy = dy//steps
		x = i[0]
		y = i[1]
		for k in range(steps-1):
			x+=dx
			y+=dy
			if (x,y) in asteroids:
				break
		else:
			count+=1
	if count>best:
		best = count
		laser = i

print(best)
print(laser)
lasx,lasy = laser

vecs = []

for x,y in asteroids:
	if x==lasx and y==lasy:
		continue
	dx = abs(x-lasx)
	dy = abs(y-lasy)
	steps = math.gcd(dx,dy)
	dx = (x-lasx)//steps
	dy = (y-lasy)//steps
	if (dx,dy) not in vecs:
		vecs.append((dx,dy))

def quadrant(x,y):
	if x>=0 and y<0:
		return 0
	if x>0 and y>=0:
		return 1
	if x<=0 and y>0:
		return 2
	return 3

def score(x,y,quadrant):
	if x==0 or y==0:
		return -99999999999999999
	else:
		result = abs(y)/abs(x)
	if quadrant%2==0:
		return -result
	else:
		return result

def compare(v1,v2):
	global lasx
	global lasy
	x1,y1 = v1
	x2,y2 = v2
	quad1 = quadrant(x1,y1)
	quad2 = quadrant(x2,y2)
	if quad1!=quad2:
		return quad1-quad2
	return score(x1,y1,quad1)-score(x2,y2,quad2)

vecs = sorted(vecs, key=cmp_to_key(compare))

"""
grid = [["   " for x in range(len(data[0]))] for y in range(len(data))]

for i,v in enumerate(vecs):
	x,y = v
	output = str(i)
	while len(output)<3:
		output = "0"+output
	grid[y+lasy][x+lasx] = output

grid[lasy][lasx] = "***"

for i in grid:
	print(i)
"""
hits = []
asteroids = list(asteroids.keys())
asteroids.remove(laser)

while len(asteroids)>0:
	for i in vecs:
		dx,dy = i
		x = lasx
		y = lasy
		while 0<=x<len(data[0]) and 0<=y<len(data):
			x+=dx
			y+=dy
			if (x,y) in asteroids:
				hits.append((x,y))
				asteroids.remove((x,y))
				break

print(hits[199][0]*100+hits[199][1])
