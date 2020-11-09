class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def get_length(head):
    slow = fast = head

    # now move fast as 2x

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return helper(slow)

    return 0


def helper(root):
    cur = root

    length = 0

    while True:
        cur = cur.next
        length += 1

        if cur == root:
            break
    return length


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle length = : " + str(get_length(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle length = : " + str(get_length(head)))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle length = : " + str(get_length(head)))
