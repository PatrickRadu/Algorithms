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

def removeNodeFromEnd(head:ListNode,n):
    dummy=ListNode(0,head)
    first,second=head,dummy
    while n:
        first=first.next
        n-=1
    while first:
        first=first.next
        second=second.next
    second.next = second.next.next
    return dummy.next

list1=create_linked_list([1,2])
print_linked_list(removeNodeFromEnd(list1,1))