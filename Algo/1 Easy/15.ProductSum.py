#[5,2,[7,-1],3,[6,[-13,8],4]]
# 12

def productSum(array, multiplier=1):
    sum = 0
    for element in array:
        if type(element) == list:
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

result = productSum([5,2,[7,-1],3,[6,[-13,8],4]])  # Example usage
print(result)  # Output: 12