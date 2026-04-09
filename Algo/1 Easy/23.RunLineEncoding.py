def runLineEncoding(s):
    if not s:
        return ""
    
    encoded_string = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_string.append(str(count) + s[i - 1])
            count = 1
            
    # Append the last run
    encoded_string.append(str(count) + s[-1])
    
    return ''.join(encoded_string)

# Example usage
print(runLineEncoding("aaabbcaaa"))  # Output: "3a2b1c3a"
