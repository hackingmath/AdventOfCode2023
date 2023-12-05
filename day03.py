
import time

start = time.time()

with open('day03test4.txt') as fp:
    lines = [x.strip() for x in fp.readlines()]
    print(lines)
    ROWS = len(lines)
    COLS = len(lines[0])
    print('ROWS,COLS:',ROWS,COLS)
    symbdict = dict()
    symbnums = dict()
    #save non-numeric, non-period symbols and locations
    numdict = dict()
    #Save numbers as ints, and save all digits locations
    reading_digits = False
    for i,row in enumerate(lines):
        for j,v in enumerate(row):

            if v.isdigit():
                if not reading_digits:
                    reading_digits = True
                    numstr = v
                    k = 1
                    while j + k < COLS and row[j+k].isdigit():
                        numstr+= row[j+k]
                        k += 1
                    num = int(numstr)
                    if num in numdict:
                        numdict[num].append([(i,c) for c in range(j,j+len(numstr))])
                    else:
                        numdict[num] = list()
                        numdict[num].append([(i,c) for c in range(j,j+len(numstr))])
                else:
                    continue
            else: #not a digit
                if reading_digits:
                    reading_digits = False
                if v == '.':
                    continue
                if v in symbdict:
                    symbdict[v].append((i,j))
                else:
                    symbdict[v] = [(i,j)]
    print(numdict)
    print(len(symbdict),symbdict)
    print("symbols:",[x for x in symbdict])

def checkSymbols(loc):
    """.
    Check all locations surrounding each digit and check any
    symbols which are adjacent."""
    for r,c in loc:
        print("r,c:",r,c)
        if r > 0:
            if lines[r-1][c] in symbdict: #UP
                    return True, COLS*(r-1)+c
            if c > 0:
                if lines[r-1][c-1] in symbdict: #UP LEFT
                    return True, COLS*(r-1)+c-1
            if c < COLS - 1:
                if lines[r-1][c+1] in symbdict: #UP RIGHT
                    return True, COLS*(r-1)+c+1
        if c > 0:
            if lines[r][c-1] in symbdict: #LEFT
                return True, COLS*r+c-1
        if c < COLS - 1:
            if lines[r][c + 1] in symbdict: #RIGHT
                return True, COLS*r+c+1
        if r < ROWS - 1:
            if lines[r+1][c] in symbdict: #DOWN
                return True, COLS*(r+1)+c
            if c > 0:
                if lines[r+1][c-1] in symbdict: #DOWN LEFT
                    return True, COLS*(r+1)+c-1
            if c < COLS - 1:
                if lines[r+1][c+1] in symbdict: #DOWN RIGHT
                    return True, COLS*(r+1)+c+1
    return False


def part1():
    output = 0
    for n in numdict:
        #print("numdict[n]:",numdict[n])
        for loc in numdict[n]:
            #print("loc:",loc)
            # for pt in loc:
            #     print("pt:",pt)
            if checkSymbols(loc):
                print("yes:",n,loc)
                output += n
            else:
                print("no:",n,loc)
    return output

def part2():
    output = 0
    for n in numdict:
        # print("numdict[n]:",numdict[n])
        for loc in numdict[n]:
            # print("loc:",loc)
            # for pt in loc:
            #     print("pt:",pt)
            if checkSymbols(loc):
                s = checkSymbols(loc)[1]
                #print("s",s)#("yes:", n, loc)
                if s in symbnums:
                    symbnums[s].append(n)
                else:
                    symbnums[s] = [n]
    for s in symbnums:
        print(symbnums[s])
        if len(symbnums[s]) == 2:
            output += symbnums[s][0]*symbnums[s][1]
    return output

#print("Part 1:",part1()) #330484 too low, 884542 too high, 537939 nope. 540025 check

print("Part 2:",part2()) #84584891
print("Time:",round(time.time()-start,1))