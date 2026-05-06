def longestPeak(array):
    maxPeakLength = 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            leftIdx = i - 2
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1
            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1
            peakLength = rightIdx - leftIdx - 1
            maxPeakLength = max(peakLength, maxPeakLength)
    return maxPeakLength


# Test Cases
print(longestPeak([1, 2, 3, 3, 4,  0, 10, 6, 5, -1, -3, 2, 3]))  # 6
