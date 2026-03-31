def binarySearch(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage
nums = [1, 2, 3, 4, 5]
target = 3
result = binarySearch(nums, target) 
print(result)  # Output: 2 (the index of the target in the array)

def binarySearchRec(nums, target):
    return binarySearchHelper(nums, target, 0, len(nums) - 1)

def binarySearchHelper(nums, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binarySearchHelper(nums, target, mid + 1, right)
    else:
        return binarySearchHelper(nums, target, left, mid - 1)  
    

# Example usage
nums = [1, 2, 3, 4, 5]      
target = 3
result = binarySearchRec(nums, target)  
print(result)  # Output: 2 (the index of the target in the array)