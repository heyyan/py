def monotonicArray(arr):
    is_non_decreasing = True
    is_non_increasing = True

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            is_non_decreasing = False
        if arr[i] > arr[i - 1]:
            is_non_increasing = False

    return is_non_decreasing or is_non_increasing 