# input = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
# input = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
# 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
# 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
# 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
# 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

file = open('day2input.txt', 'r')
input = []
for line in file.read().splitlines():
    input.append(line)
file.close()

# bag contains 12 red cubes, 13 green cubes, and 14 blue cubes - what's the best data structure to represent this
# declare variable possibleGames and initialize it at 0
# iterate over games
    # create list of lists for subset, split input at ","
    # compare subset quantity for every color with original quantity in the bag
        # if quantity is smaller or equal to original quantity add it to possibleGames

def parseData(data):
    divideGameAndSubsets = [line.split(":") for line in data]
    return [game[1].split(";") for game in divideGameAndSubsets]

inputData = parseData(input)

#cubes
availableCubes = {"red": 12, "green": 13, "blue": 14}

# create a dictionary for every subset for each game
# Game 1: [{blue:3, red:4}, {red:1, green:2, blue:6}]
# input: ' 3 blue, 4 red' 
# output: {blue:3, red:4}
def createDictionary(string):
    subset = {}
    stringIntoArray = string.split(",")
    for item in stringIntoArray:
        keyValue = item.split() # split method without any delimeters will split based on data structures
        subset[keyValue[1]] = int(keyValue[0])
    return subset

# creates list of dictionaries for subsets for every game
# input: ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
# output: [{blue: 3, red:4}, {red:1, green:2, blue:6}, {green:2}]
def listOfDicts(subsets):
    return [createDictionary(item) for item in subsets] #list comprehension, mapping

# check if a game is possible
# input: [{blue: 3, red:4}, {red:1, green:2, blue:6}, {green:2}]
# output: boolean
def isPossible(listOfSubsets):
    for subset in listOfSubsets:     
        for color in subset.keys():
            if(subset[color] > availableCubes[color]):
                return False
    return True

# input: [['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']]
# output: int
def possibleGames(input):
    games = [listOfDicts(item) for item in input]
    sumOfIds = 0
    for index, game in enumerate(games):
        if isPossible(game) == True:
            sumOfIds += (index+1)
    return sumOfIds   

print(possibleGames(inputData))
