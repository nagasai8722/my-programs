class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.prev = None 
 
def printLeftToRightManner(head):
    print("Left to Right")
    curr = head 
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next 
    print()
 
def printRightToLeftManner(head):
    print("Right to Left")
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.prev 
    print()
 
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    newBlock.prev = tail 
    return head
 
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
     
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock
 
def insertAtSpecificPosition(head, val, position):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position - 1:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
    
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
 
    
    curr.next = newBlock 
    newBlock.prev = curr 
 
   
 
    return head
 
def deleteTailNodeInDoublyLinkedList(head):
    if head == None or head.next == None:
        return None 
    
    curr, previous = head, None
    while curr.next != None:
        previous = curr 
        curr = curr.next 
    
    previous.next = None 
    curr.prev = None 
    return head 
 
def deleteHeadNodeInDoublyLinkedList(head):
    if head == None or head.next == None:
        return None 
   
    secondNode = head.next 
    head.next = None 
    secondNode.prev = None 
    return secondNode 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInDoublyLinkedList(head)
    
 
    curr = head 
    index = 1 
 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    nodeToBeDeleted = curr.next 
    nextNode = nodeToBeDeleted.next 
    curr.next = nextNode 
    nextNode.prev = curr 
    return head
 
l = [11, 22, 33, 44, 55, 66, 77]
head = None 
for ele in l:
    
    head = addNodeAtHeadOfLinkedList(head, ele)
 
printLeftToRightManner(head)
printRightToLeftManner(head)   
 

head = deleteNodeAtSpecificPosition(head, 4)
 
printLeftToRightManner(head)
printRightToLeftManner(head)
 
