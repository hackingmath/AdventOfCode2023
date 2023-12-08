
import time
from collections import defaultdict

start = time.time()


CATSTRENGTH = ['highcard', 'pair', 'pair2', 'kind3','fullh', 'kind4', 'kind5']
categories = {'highcard': [],
              'pair': [],
              'pair2': [],
              'kind3': [],
              'fullh': [],
              'kind4': [],
              'kind5': []}

with open('day07.txt') as fp:
    lines = [x.strip() for x in fp.readlines()]
    #print(lines)
    hands = [line.split(' ') for line in lines]
    #print(hands)
    bids = {hand[0]: int(hand[1]) for hand in hands}
    print(bids)

def categorize(hand):
    #create count dict
    count_dict = defaultdict()
    for i,v in enumerate(hand):
        if v in count_dict:
            count_dict[v] += 1
        else:
            count_dict[v] = 1
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 'kind5'
    if 4 in count_dict.values():
        return 'kind4'
    if 3 in count_dict.values():
        if 2 in count_dict.values():
            return "fullh"
        else:
            return "kind3"
    cvals = [v for v in count_dict.values()]
    if cvals.count(2) == 2:
        return 'pair2'
    if cvals.count(2) == 1:
        return 'pair'
    return 'highcard'

def compare(a,b,s):
    """Compares two hands by comparing
    the corresponding cards in order"""
    for i,v in enumerate(a):
        if s.index(v) > s.index(b[i]):
            return b
        if s.index(v) < s.index(b[i]):
            return a

def bubble_sort(arr,s):
    for _ in range(len(arr)-1):
        for i in range(len(arr)-1):
            if compare(arr[i],arr[i+1],s) != arr[i]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                #print(arr)
    return arr

def part1():
    STRENGTH = '23456789TJQKA'
    winnings = 0
    for hand in hands:
        #print(hand)
        categories[categorize(hand[0])].append(hand[0])
    #print(categories)
    rank = 1
    for c in CATSTRENGTH:
        #print("category:",c)
        if categories[c]:
            categories[c] = bubble_sort(categories[c],STRENGTH)
            #print(rank,h,bids[h])
            #print(categories)
            for h in categories[c]:
                #print("h:",h)
                winnings += rank*bids[h]
                rank += 1
    return winnings


def part2OLD():
    STRENGTH = 'J23456789TQKA' #J is now lowest
    winnings = 0
    changed = False
    for hand in hands:
        #print("hand:",hand)
        #make J optimal character
        if "J" in hand[0]:
            #print("j in hand")
            possible_category = categorize(hand[0])
            best = 'J'
            besthand = hand[0]
            for char in hand[0]:
                if char != 'J':
                    newhand = hand[0].replace("J",char)
                    #print("newhand,best:",newhand,best)
                    newcat = categorize(newhand)
                    #print("new category:",newcat)
                    if CATSTRENGTH.index(categorize(newhand)) > CATSTRENGTH.index(possible_category):
                        #print("newbest")
                        best = char
                        besthand = newhand
                        possible_category = newcat
                        changed = True
            if changed:
                if besthand not in bids:
                    bids[besthand] = bids[hand[0]]
                categories[possible_category].append(hand[0])
                #categories[categorize(hand[0])].remove(hand[0])
                changed = False
        else:
            categories[categorize(hand[0])].append(hand[0])
            #print("elsecategories",categories)

    #print("newcats:",categories)
    rank = 1
    ranking = list()
    for c in CATSTRENGTH:
        #print("category:",c)
        if categories[c]:
            categories[c] = bubble_sort(categories[c],STRENGTH)
            #print(rank,h,bids[h])
            #print(categories)
            for h in categories[c]:
                #print("h:",h)
                ranking.append([])
                winnings += rank*bids[h]
                ranking[rank-1].append(h)
                ranking[rank-1].append(bids[h])
                rank += 1
    winnings_test = 0
    for i,hand in enumerate(ranking):
        winnings_test += (i+1)*hand[1]
    print("ranking:",ranking)
    print("test winnings:",winnings_test)
    return winnings

def part2():
    STRENGTH = 'J23456789TQKA' #J is now lowest
    winnings = 0
    changed = False
    for hand in hands:
        #print("hand:",hand)
        #make J optimal character
        if "J" in hand[0]:
            if hand[0].count("J") == 5:
                categories[categorize(hand[0])].append(hand[0])
                continue
            #print("j in hand")
            #count J's and max of other letter
            letter_count = {letter:hand[0].count(letter) for letter in hand[0]}
            sorted_letters = sorted(letter_count.items(), key=lambda x:x[1], reverse=True)
            # print(hand[0])
            # print(letter_count)
            # print(sorted_letters)
            if sorted_letters[0][0] == 'J':
                replace_letter = sorted_letters[1][0]
            else:
                replace_letter = sorted_letters[0][0]
            newhand = hand[0].replace("J", replace_letter)
            newcat = categorize(newhand)
            categories[newcat].append(hand[0])
        else:
            categories[categorize(hand[0])].append(hand[0])
    #print(categories)
    rank = 1
    ranking = list()
    for c in CATSTRENGTH:
        #print("category:",c)
        if categories[c]:
            categories[c] = bubble_sort(categories[c],STRENGTH)
            #print(rank,h,bids[h])
            #print(categories)
            for h in categories[c]:
                #print("h:",h)
                ranking.append([])
                #print("rank,bids[h]:",rank,bids[h])
                winnings += rank*bids[h]
                ranking[rank-1].append(h)
                ranking[rank-1].append(bids[h])
                rank += 1
    #print(ranking)
    return winnings

#print(compare('33332','2AAAA'))
#print("sorttest:",bubble_sort(['33332','2AAAA','T2222','84444','4QQQQ']))
#print("Part 1:",part1())

print("Part 2:",part2()) #245876162 too high
print("Time:",round(time.time()-start,1))