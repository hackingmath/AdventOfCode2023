
import time

start = time.time()
NUMS = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

with open("day01.txt") as f:
    oplist1 = f.readlines() #list of strings


def part1():
    numlist = list()
    output = 0
    first, last = None, None
    for i, string in enumerate(oplist1):
        #numlist.append([])


        for c in string:
            if c in '01234567890':
                first = c
                break
        for c in string[::-1]:
            if c in '01234567890':
                last = c
                break

                #numlist[i].append(c)

        output += int(first+last)
    return output

def part2():
    output = 0

    for string in oplist1:
        first, last, foundFirst, foundLast = None, None, False, False
        for j, c in enumerate(string):
            if c in '01234567890':
                first = c
                foundFirst = True
                break
            if foundFirst:
                break
            # check if c is first letter of number in NUMS:
            for n in NUMS:
                if c == n[0]:
                    if string[j:j + len(n)] == n:
                        first = str(NUMS[n])
                        #print("first str:",first)
                        foundFirst = True
                        break
                if foundFirst:
                    break

        for j in range(len(string)-1,-1,-1):
            if string[j] in '01234567890':
                last = string[j]
                break
            for n in NUMS:
                if j + len(n) > len(string)-1:
                    #print("over length:",j,n)
                    continue
                if string[j:j + len(n)] == n:
                    last = str(NUMS[n])
                    #print("last str:",last)
                    foundLast = True
                    break
            if foundLast:
                break
        #print("first,last:",first,last)
        output += int(first+last)
    return output

def part2OLD():
    numlist = list()
    for i, string in enumerate(oplist1):
        numlist.append([])
        for j,c in enumerate(string):
            if c in '01234567890':
                numlist[i].append(c)
            #check if c is first letter of number in NUMS:
            for n in NUMS:
                if c == n[0]:
                    if string[j:j+len(n)] == n:
                        numlist[i].append(str(NUMS[n]))
    print(numlist)
    output = 0
    for arr in numlist:
        output += int(arr[0] + arr[-1])
    return output


print("part1:",part1())

print("part2:",part2())
print("Time:",time.time()-start)