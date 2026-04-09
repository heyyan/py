def generateDocument(characters, document):
    charactersCount = {}
    for character in characters:
        if character not in charactersCount:
            charactersCount[character] = 0
        charactersCount[character] += 1

    for character in document:
        if character not in charactersCount or charactersCount[character] == 0:
            return False
        charactersCount[character] -= 1

    return True

# Example usage
print(generateDocument("Bste!hetsi ogEAxpelrt x ", "AlgoExpert"))  # Output: True   