def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx += 1
    return array    

# Example usage
array = [5, 1, 4, 2, 8] 
sorted_array = selectionSort(array)
print(sorted_array)  # Output: [1, 2, 4, 5, 8]  