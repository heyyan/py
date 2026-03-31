def maxSpeed(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        blueShirtSpeeds.reverse()

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return totalSpeed


result = maxSpeed([5, 3, 9, 2, 1], [7, 6, 4, 5, 2], True)
print(result)  # Output: 32
