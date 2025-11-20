class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def NodeDepth(node, depth=0):
    if node is None:
        return 0
    return depth + NodeDepth(node.left, depth + 1) + NodeDepth(node.right, depth + 1 )

def nodeDepthsInterative(root):
    sumOFDepths = 0
    stack = [{"node": root, "depth": 0}]
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node, depth = nodeInfo["node"], nodeInfo["depth"]
        if node is None:
            continue
        sumOFDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
    return sumOFDepths

root = BST(1)
root.left = BST(2)
root.right = BST(3)
root.left.left = BST(4)
root.left.right = BST(5)    
root.right.left = BST(6)
root.right.right = BST(7)
result = nodeDepthsInterative(root)