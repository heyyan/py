def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList
    while currentNode is not None:
        nextDistinctNode = currentNode.next
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = nextDistinctNode
    return linkedList

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


root = LinkedList(1)
root.next = LinkedList(1)   
root.next.next = LinkedList(3)
root.next.next.next = LinkedList(4) 
root.next.next.next.next = LinkedList(4)
result = removeDuplicatesFromLinkedList(root)  # Example usage

print(result)  # Output: None