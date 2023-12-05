
import time
from collections import defaultdict

start = time.time()

with open('day04.txt') as fp:
    data = [x.strip().split(":") for x in fp.readlines()]
    #print(data)
    lines = [d[1].split('|') for d in data]
    #print(lines)
    cards = list()
    for line in lines:
        g1,g2 = line[0].split(" "),line[1].split(" ")
        g1 = [int(x) for x in g1 if x.isdigit()]
        g2 = [int(x) for x in g2 if x.isdigit()]
        cards.append([g1,g2])
    #print(cards)

def part1():
    output = 0

    for card in cards:
        doubles = 0
        value = 0
        g1,g2 = card
        #print(g1,g2)
        for num in g1:
            if num in g2:
                #print("num:",num)
                if doubles == 0:
                    doubles += 1
                    value = 1
                else:
                    value *= 2
        output += value
    return output

def part2():
    output = 0
    matchdict = defaultdict(int)
    cardlist = [i for i in range(len(cards))]
    for i,card in enumerate(cards):
        matches = 0
        g1, g2 = card
        # print(g1,g2)
        for num in g1:
            if num in g2:
                # print("num:",num)
                matches += 1
        matchdict[i] = matches
    #print(matchdict)
    for i in range(len(cards)):
        for k in range(1,cardlist.count(i)+1):
            for j in range(i+1,i+matchdict[i]+1):

                cardlist.append(j)
    #print(cardlist)
    return len(cardlist)



    return output

#print("Part 1:",part1())

#print("Part 2:",part2())
print("Time:",round(time.time()-start,1))