def validateSubsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0

    while arr_idx < len(array) and seq_idx < len(sequence):
        if array[arr_idx] == sequence[seq_idx]:
            seq_idx += 1
        arr_idx += 1

    return seq_idx == len(sequence)


def validateSubsequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)
result = validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])
print(result)  # Output: True