class Node:
    def __init__(self, name):
        self.children = []
        self.name = name
    
    def addChild(self, name):
        self.children.append(Node(name))
    
def depthFirstSearch(node, array):
    array.append(node.name)
    for child in node.children:
        depthFirstSearch(child, array)
    return array

# Example usage:
root = Node("A")    
root.addChild("B")
root.addChild("C")
root.addChild("D")
root.children[0].addChild("E")  
root.children[0].addChild("F")
root.children[2].addChild("G")  
root.children[2].addChild("H")
root.children[0].children[1].addChild("I")  
root.children[0].children[1].addChild("J")
result = depthFirstSearch(root, [])
print(result)  # Output: ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'H']
