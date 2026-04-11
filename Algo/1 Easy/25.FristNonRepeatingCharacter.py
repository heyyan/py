def firstNonRepeatingCharacter(s):
    char_count = {}
    
    # Count the occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    # Find the first non-repeating character
    for char in s:
        if char_count[char] == 1:
            return char
            
    return None  # Return None if there is no non-repeating character

# Example usage
print(firstNonRepeatingCharacter("abcdcaf"))  # Output: 'b'