def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets

# Test cases
print(threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0))  # [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
print(threeNumberSum([1, 2, 3], 6))  # [[1, 2, 3]]
print(threeNumberSum([1, 2, 3], 7))  # []
print(threeNumberSum([8, 10, -2, 49, 14 ], 57))  # [[-2, 10, 49]]