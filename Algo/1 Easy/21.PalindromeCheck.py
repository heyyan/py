def isPalindrome(string):
    reversedString = ""
    for i in range(len(string)):
        reversedString += string[i]
    return string == reversedString


# Example usage
print(isPalindrome("racecar"))  # Output: True


def isPalindrome(string):
    reversedChars = []
    for i in range(len(string)):
        reversedChars.append(string[i])
    return string == "".join(reversedChars)


# Example usage
print(isPalindrome("hello"))  # Output: False


def isPalindrome(string, i=0):
    j = len(string) - 1 - i
    if i >= j:
        return True
    if string[i] != string[j]:
        return False
    return isPalindrome(string, i + 1)

def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1
    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False
        leftIdx += 1
        rightIdx -= 1
    return True 

# Example usage
print(isPalindrome("madam"))  # Output: True    