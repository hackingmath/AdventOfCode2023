
import time

start = time.time()

with open('day02.txt') as fp:
    lines = [x.strip().split() for x in fp.readlines()]
    print(lines)
    gamedict = dict()
    for line in lines:
        gnum = line[1][:-1]
        gamedict[gnum] = [0,0,0] #RGB :-)
        for i in range(2,len(line)-1):
            if line[i].isdigit():
                line[i] = int(line[i])
                if line[i+1].startswith("red"):
                    gamedict[gnum][0] = max(gamedict[gnum][0],line[i])
                if line[i+1].startswith("green"):
                    gamedict[gnum][1] = max(gamedict[gnum][1],line[i])
                if line[i+1].startswith("blue"):
                    gamedict[gnum][2] = max(gamedict[gnum][2],line[i])

    print(gamedict)


def part1():
    bag = [12,13,14]
    def gameWorks(g):
        #print("game:", g)
        for i in range(3):
            if gamedict[g][i] > bag[i]:
                return False
        return True

    output = 0
    for game in gamedict:
        if gameWorks(game):
            output += int(game)
    return output

def part2():
    output = 0
    for game in gamedict:
        prod = gamedict[game][0]*gamedict[game][1]*gamedict[game][2]
        output += prod
    return output

print("Part 1:",part1())

print("Part 2:",part2())
print("Time:",round(time.time()-start,1))