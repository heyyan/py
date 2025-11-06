def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) -1):
#         firstNum = array[i]
#         for j in range(i + 1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 return [firstNum, secondNum]
#     return []

# def twoNumberSum(array, targetSum):
#     num_dict = {}
#     for num in array:
#         complement = targetSum - num
#         if complement in num_dict:
#             return [complement, num]
#         num_dict[num] = True
#     return []

result = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(result)  # Output: [11, -1] or [-1, 11]