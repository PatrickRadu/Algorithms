class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def revLinkList(head:ListNode):
    prev,curr=None,head
    while curr:
        temp=curr.next
        curr.next=prev
        prev=curr
        curr=temp
    return prev

def recursiveRevLinkList(head:ListNode):
    if head==None:
        return None
    newHead=head
    if head.next:
        newHead=recursiveRevLinkList(head.next)
        head.next.next=head
    head.next=None
    return newHead


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
ll=create_linked_list([1,2,3,4])
print_linked_list(ll)
print_linked_list(revLinkList(ll))
print_linked_list(recursiveRevLinkList(ll))