def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()
    return sortedSquares


result = sortedSquaredArray([-7, -3, 1, 4, 8, 12])
print(result)  # Output: [1, 9, 16, 49, 64, 144]


def sortedSquaredArray2(array):
    sortedSquares = [0 for _ in array]
    smallerIdx = 0
    largerIdx = len(array) - 1
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerIdx]
        largerValue = array[largerIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerIdx -= 1
    return sortedSquares    

result = sortedSquaredArray2([-7, -3, 1, 4, 8, 12])
print(result)  # Output: [1, 9, 16, 49, 64, 144]