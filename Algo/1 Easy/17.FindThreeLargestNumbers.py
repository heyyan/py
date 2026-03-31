def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx):
        array[i] = array[i + 1]
    array[idx] = num    

# Example usage
array = [14,1,17,-7,-17,-27,18,541,8,7,7,7  ]  
result = findThreeLargestNumbers(array)
print(result)  # Output: [17, 18,541 ] (the three largest numbers in the array)