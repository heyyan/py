def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                isSorted = False
        counter += 1
    return array    

# Example usage
array = [5, 1, 4, 2, 8] 
sorted_array = bubbleSort(array)
print(sorted_array)  # Output: [1, 2, 4, 5, 8]  