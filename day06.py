
import time
from math import sqrt,ceil

start = time.time()

# with open('day06test.txt') as fp:
#     lines = [x.strip() for x in fp.readlines()]

testdata = [[7,15,30],[9,40,200]]
data = [[48,87,69,81],[255,1288,1117,1623]]
p2 = [48876981,255128811171623]

def quad(a,b,c):
    """Good old quadratic formula"""
    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1,x2

def part1(d):
    output = 1
    ways = [0 for x in range(len(d[0]))]
    records = d[1]
    for i,v in enumerate(d[0]):
        for speed in range(v):
            dist = speed*(v-speed)
            if dist > records[i]:
                ways[i] += 1
    for n in ways:
        output *= n
    return output

def part2_bruteforce(d):
    """Runs in 6.6 seconds"""
    output = 0
    records = d[1]
    for speed in range(d[0]):
        dist = speed * (d[0] - speed)
        if dist > records:
            output += 1
    return output

def part2(d):
    """Runs in 0.0 seconds :-)"""
    speed,record = d
    low,high = quad(-1,speed,-record)
    return int(high-low)

#print("Part 1:",part1(data))

#print("Part 2 Brute Force:",part2_bruteforce(p2)) #36992486
print("Part 2:",part2(p2))
print("Time:",round(time.time()-start,1))