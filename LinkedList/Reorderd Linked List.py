class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next
def reorderLinkedListBF(head:ListNode):
    current=head
    while current and current.next and current.next.next:
        prev=current
        while prev.next.next:
            prev=prev.next
        lastNode=prev.next
        prev.next=None
        temp=current.next
        current.next=lastNode
        lastNode.next=temp
        print("lastNode",lastNode.val)
        current=current.next.next
    return head

list1=create_linked_list([2,4,6,8])
print_linked_list(list1)
print_linked_list(reorderLinkedListBF(list1))
