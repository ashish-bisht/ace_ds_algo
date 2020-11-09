class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def find_length(head):

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return find_length_helper(slow)


def find_length_helper(root):
    cur = root

    length = 0
    while True:
        cur = cur.next
        length += 1
        if cur == root:
            return length
    return 0


def find_cycle_start(head):

    # first find length of cycle..
    length_of_cycle = find_length(head)

    slow = head
    fast = head

    while length_of_cycle > 0:
        fast = fast.next
        length_of_cycle -= 1

    while True:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            return fast

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).val))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(find_cycle_start(head).val))

head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(find_cycle_start(head).val))
