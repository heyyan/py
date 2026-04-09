def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1
    return array

# Example usage
array = [5, 1, 4, 2, 8] 
sorted_array = insertionSort(array)
print(sorted_array)  # Output: [1, 2, 4, 5, 8]  