
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def reorder(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # print(slow.value)
    second_half_head = reverse(slow)

    first_half_head = head

    while first_half_head and second_half_head:
        temp = first_half_head.next
        first_half_head.next = second_half_head
        first_half_head = temp

        # same with second

        temp = second_half_head.next
        second_half_head.next = first_half_head
        second_half_head = temp

    if first_half_head:
        first_half_head.next = None

    return head


def reverse(head):
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def display(head):
    while head:
        print(str(head.value) + " ", end='')
        head = head.next


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)

# print(display(head))

reordered_list = reorder(head)
display(reordered_list)
