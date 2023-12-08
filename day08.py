
import time
from math import sqrt

start = time.time()

directions = {"L":0,"R":1}
dirs1, dirs2,dirs3 = "RL","LLR","LR"
dirs = 'LRRLRLRRRLLRLRRRLRLLRLRLRRLRLRRLRRLRLRLLRRRLRRLLRRRLRRLRRRLRRLRLRLLRRLRLRRLLRRRLLLRRRLLLRRLRLRRLRLLRRRLRRLRRRLRRLLRRRLRRRLRRRLRLRRLRLRRRLRRRLRRLRLRRLLRRRLRRLLRRLRRLRLRLRRRLRLLRRRLRRLRRRLLRRLLLLLRRRLRRLLLRRRLRRRLRRLRLLLLLRLRRRLRRRLRLRRLLLLRLRRRLLRRRLRRRLRLRLRRLRRLRRLRLRLLLRLRRLRRLRRRLRRRLLRRRR'

with open('day08.txt') as fp:
    lines = [x.strip() for x in fp.readlines()]
    print(lines[:10])
    elem_dict = dict()
    for line in lines:
        elem,ch = line.split(" = ")
        l,r = ch[1:4],ch[6:9]
        elem_dict[elem] = (l,r)
    #print(elem_dict)

def part1(d):
    """Navigate from AAA to ZZZ"""
    loc = 'AAA'
    steps = 0
    while loc != 'ZZZ':
        direction = d[steps%len(d)]
        loc = elem_dict[loc][directions[direction]]
        print(loc)
        steps += 1
    return steps

def navigate(loc,d):
    """Navigate from AAA to ZZZ"""
    return elem_dict[loc][directions[d]]

def part2(d):
    """Brute Force. Never ends."""
    st = {v for v in elem_dict.keys() if v[-1] == 'A'}
    steps = 0
    while True:
        direction = d[steps % len(d)]
        #loc = elem_dict[loc][directions[direction]]
        st = {navigate(v,direction) for v in st}
        #print(st)
        steps += 1
        if all({v.endswith('Z') for v in st}):
            return steps

def lcm1(arr):
    prod = 1
    for n in arr:
        prod*= n
    mults = [set() for n in arr]
    m = 1
    while True:

        for i,v in enumerate(arr):
            mults[i].add(v*m)

        for n in mults[0]:
            if all([n in marr for marr in mults]):
                return n
        m += 1
        if m % 1000 == 0:
            for x in mults:
                print(x)


def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def factorList(n):
    output = list()
    for i in range(2,n+1):
        if n % i == 0 and isPrime(i):
            while n % i == 0:
                output.append(i)
                n //= i

    return output

def lcm(arr):
    factorlists = [factorList(n) for n in arr]
    factors = list()
    for l in factorlists:
        for n in l:
            while factors.count(n) < l.count(n):
                factors.append(n)
    output = 1
    #print('factorset:',factors)
    for n in factors:
        output *= n
    return output

def part2LoopTest(d):
    st = {v for v in elem_dict.keys() if v[-1] == 'A'}
    print("st:",st)
    loops = list()
    for i,v in enumerate(st):
        #steps = 0
        loops.append(list())
        for s in range(500000):
            direction = d[s % len(d)]
            v = navigate(v,direction)
            #steps += 1
            #print("v:",v)
            if v.endswith('Z'):
                loops[i].append(s+1)
    prod = 1
    firsts = list()
    for loop in loops:
        print(loop)
        first = loop[0]
        firsts.append(first)
        # b,n = isPrime(first)
        # prod*=n
    print("firsts:",firsts)
    lcm1 = lcm(firsts)
    print("lcm:",lcm1)
    return lcm1


#print("Part 1:",part1(dirs))
#print(factorList(20))
#print(lcm([2,3,5,7,20]))
print("Loop Test:",part2LoopTest(dirs))

#I tried taking all the first step numbers each starting point
#took to get to Z and multiplying them together but it was too high.
# Then I found the lowest prime factor of each.
# Multiplied them all but it was too low.
#"Part 2:",part2(dirs) 71958382637 too low. 21083806112641 correct.
print("Time:",round(time.time()-start,1))