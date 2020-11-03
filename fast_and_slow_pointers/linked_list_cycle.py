class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = fast = head

    ## now move fast as 2x

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(has_cycle(head)))

