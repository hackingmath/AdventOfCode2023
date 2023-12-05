
import time

start = time.time()

with open('day05.txt') as fp:
    lines = [x.strip().split('\n\n') for x in fp.readlines()]
    #maps = lines
    #print(lines)
    seedlist = [int(x) for x in lines[0][0].split(":")[1].split(' ') if x != '']
    #print(seedlist)
    mlists = list()
    new = True
    for line in lines:
        if line == ['']: continue
        if not line[0][0].isdigit():
            if not new:
                mlists.append(newlist)
                new = True
                continue
            else:
                continue
        if new:
            newlist = [[int(x) for x in line[0].split(' ')]]
            new = False
        else:
            newlist.append([int(x) for x in line[0].split(' ')])
    #newlist.append([int(x) for x in lines[-1][0].split(' ')])
    mlists.append(newlist)
    #print(mlists)



def fmap(n,maplist):
    """Takes in number, runs through maplist
    """
    for a,b,c in maplist:
        if n in range(b,b+c):
            return a + (n-b)
    return n

def backmap(n,maplist):
    """Runs a number backward through a maplist"""
    for a,b,c in maplist:
        if n in range(a,a+c):
            return b + (n-a)
    return n

def part1(seedlist):
    loclist = list()
    for n in [13]:#seedlist:
        #print(n)
        for maplist in mlists:
            #print(n)
            n = fmap(n,maplist)
        #print(n)
        loclist.append(n)
    return min(loclist)


def part2OLD():
    lowest = 1e12
    slists = list()
    for i in range(0,len(seedlist),2):
        #slists.append([seedlist[i]+ n for n in range(seedlist[i+1]) ]
        slists.append([seedlist[i], seedlist[i] + seedlist[i + 1]])
    print("slists:",slists)
    for slist in slists:
        print(slist)
        p1 = part1(slist)
        print("p1:",p1)
        lowest = min(lowest,p1)
    possible_range = [3007537707, 3511520874]
    slist1 = [x for x in range(possible_range[0],possible_range[1]+1)]
    rangemin = part1(slist1)
    print("rangemin:",rangemin)
    return lowest

def part2():
    slists = list()
    for i in range(0, len(seedlist), 2):
        #slists += [seedlist[i]+ n for n in range(seedlist[i+1]) ]
        slists.append([seedlist[i], seedlist[i] + seedlist[i + 1]])
    print(slists)
    startn, n = 0,0
    while True:
        n = startn
        #print("startn:",n)
        for m in mlists[::-1]:
            n = backmap(n,m)
        #print("backmappedn:",n)
        for s in slists:
            if s[0] <= n <= s[1]:
            # if n in slists:
                print(n,"in slist")
                return startn
        startn += 1
        #n += 1
        if startn% 100000 == 0:
            print("startn:",startn)
    return None


print("Part 1:",part1(seedlist=seedlist))

print("Part 2:",part2()) #113469887 too high
print("Time:",round(time.time()-start,1))