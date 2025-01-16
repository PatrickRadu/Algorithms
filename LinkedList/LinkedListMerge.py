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

list1=create_linked_list([1,2,4])
list2=create_linked_list([1,3,5])

print_linked_list(list1)
print_linked_list(list2)

def mergeSortedLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Create a dummy node to act as the starting point
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2
    return dummy.next


print_linked_list(mergeSortedLists(list1,list2))