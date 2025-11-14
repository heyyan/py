def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree, target, float("inf"))  

def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBSTIterative(tree, target):
    closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example usage:
# Creating a sample BST 
root = BST(10)
root.left = BST(5)  
root.right = BST(15)
root.left.left = BST(2)     
root.left.right = BST(5)
root.right.right = BST(22)
root.left.left.left = BST(1)
result = findClosestValueInBST(root, 12)

print(result)  # Output: inf