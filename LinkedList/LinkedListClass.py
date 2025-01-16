class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            return
        position = 0
        curr_node = self.head
        while (curr_node != None and position + 1 != index):
            position += 1
            curr_node = curr_node.next
            if curr_node != None:
                new_node = ListNode(data)
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = ListNode(data)
        if self.head == None:
            self.head = new_node
            return
        currentNode = self.head
        while (currentNode.next):
            currentNode = currentNode.next
        currentNode.next = new_node
    def remove_first_node(self):
        if (self.head == None):
            return
        else:
            self.head = self.head.next