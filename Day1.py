file = open('day1input.txt', 'r')
fileInput = []
for line in file.readlines():
    fileInput.append(line)
file.close()

# one = "tlbtwo62five"
# input = ["two1nine",
# "eightwothree",
# "abcone2threexyz",
# "xtwone3four",
# "4nineeightseven2", 
# "zoneight234", 
# "7pqrstsixteen"]


def findDigit(string):
    digitsLetters = {"one": "1", "two": "2", "three": "3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    index = 0
    for index in range(len(string)-1):
        for digit in digitsLetters.keys():
            if string.startswith(digit, index):
                return digitsLetters[digit]    
        if string[index].isnumeric():
            return string[index]
        
# answer for Day 1 part 1
# def calibrationValue(string):
#     return findDigit(string) + findDigit(string[::-1])

#answer to Day 1 part 2
def findLastDigit(string):
    digitsLetters = {"one": "1", "two": "2", "three": "3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    stringLength = len(string)
    i = 1
    while i <= stringLength:
        for digit in digitsLetters.keys():
            # slice = string[-i:]
            if string[-i:].startswith(digit):
                return digitsLetters[digit]
        if string[-i].isnumeric():
            return string[-i]
        i += 1

# answer for Day 1 part 2
def calibrationValue(string):
    calVal = findDigit(string) + findLastDigit(string)
    return calVal

def inputToCalibrationValues(inputArray):
    listCalibrationValues = []
    for string in inputArray:
        listCalibrationValues.append(calibrationValue(string))
    return listCalibrationValues


def addValues(valuesArray):
    calibrationValuesArray = inputToCalibrationValues(valuesArray)
    sumOfValues = 0
    for val in calibrationValuesArray:
        sumOfValues += int(val)
    return sumOfValues

print(addValues(fileInput))  
# print(addValues(input)) 
# print(calibrationValue(one))

