class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums
def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)

root = BST(1)
root.left = BST(2)
root.right = BST(3)
root.left.left = BST(4)
root.left.right = BST(5)
root.right.left = BST(6)
root.right.right = BST(7)
result = branchSums(root)
print(result)  # Output: [7, 8, 10, 11]    