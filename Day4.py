# "card = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
# listOfCards = [
# "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
# "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
# "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
# "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
# "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
# "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
# ]

file = open('day4input.txt', 'r')
listOfCards = []
for line in file.read().splitlines():
    listOfCards.append(line)
file.close()

# input: ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"]
# output: [[[41, 48, 83, 86, 17],[83, 86, 6, 31, 17, 9, 48, 53]], [[13 32 20 16 61],[61, 30, 68, 82, 17, 32, 24, 19]]
def parseData(data):
    card = [line.split(':') for line in data]
    nums = [item[1].split('|') for item in card]
    output = []
    for list in nums:
        listOfNums = []
        winningNumsStr = list[0].split()
        myNumsStr = list[1].split()
        listOfNums.append([int(val) for val in winningNumsStr])
        listOfNums.append([int(val) for val in myNumsStr])
        output.append(listOfNums)
    return output

# input: [41, 48, 83, 86, 17] [83, 86, 6, 31, 17, 9, 48, 53]
# output: int -> 4
def howManyWinningNums(winNums, myNums):
    counter = 0
    for num in winNums:
        if num in myNums:
            counter += 1
    return counter

# input: 4
# output: 8
def pointsPerCard(numOfWinningNums):
    points = 0
    for num in range(0, numOfWinningNums + 1):
        if num == 1:
            points = 1 # first match is worth 1 point
        else:
            points *= 2 # each match after the first double the point value of the card
    return points

# input: ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"]
# output: 13
def totalValCards(data):
    cards = parseData(data)
    totalPoints = 0
    for winningNumbers, myNumbers in cards:
        cardWinningNums = howManyWinningNums(winningNumbers, myNumbers)
        cardPoints = pointsPerCard(cardWinningNums)
        totalPoints += cardPoints
    return totalPoints

print(totalValCards(listOfCards))