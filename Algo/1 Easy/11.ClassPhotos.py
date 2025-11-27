def photo(red, blue):
    red.sort()
    blue.sort()

    if red[0] < blue[0]:
        front_color = 'red'
    else:
        front_color = 'blue'

    for r, b in zip(red, blue):
        if front_color == 'red' and r >= b:
            return False
        if front_color == 'blue' and b >= r:
            return False

    return True

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reversed=True)
    blueShirtHeights.sort(reversed=True)
    shirtColorInFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'  
    for idx in range(len(redShirtHeights)):
        redHeight = redShirtHeights[idx]
        blueHeight = blueShirtHeights[idx]
        if shirtColorInFirstRow == 'RED':
            if redHeight >= blueHeight:
                return False
        else:
            if blueHeight >= redHeight:
                return False    
    return True  

result = photo([5, 8, 1, 3, 4], [6, 9, 2, 4, 5])
print(result)  # Output: True   