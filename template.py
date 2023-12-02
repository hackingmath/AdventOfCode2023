
import time

start = time.time()

with open('day02.txt') as fp:
    lines = [x.strip() for x in fp.readlines()]

def part1():
    pass

def part2():
    pass

#print("Part 1:",part1())

#print("Part 2:",part2())
print("Time:",round(time.time()-start,1))