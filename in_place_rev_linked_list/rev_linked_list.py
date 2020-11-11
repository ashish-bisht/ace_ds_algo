
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def display(head):
    while head:
        print(head.value)
        head = head.next


def reverse(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)

display(head)
reversed_lst = reverse(head)
display(reversed_lst)
