class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def display(head):
    while head:
        print(head.value, end=" ")
        head = head.next


def reverse(cur, count):
    prev = None

    while cur and count:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
        count -= 1
    return prev


def reverse_sub_list(head, p, q):

    cur = head
    prev = None

    # after skipping 'p-1' nodes, current will point to 'p'th node
    i = 0
    while cur and i < p-1:
        prev = cur
        cur = cur.next
        i += 1

    print(prev.value)
    first_part = prev

    part_to_reverse = cur

    # get third part
    i = 0
    while cur and i < q-p+1:
        cur = cur.next
        i += 1

    third_part = cur

    second_part = reverse(part_to_reverse, q-p+1)

    # Join all parts
    cur = second_part

    while cur.next:
        cur = cur.next

    cur.next = third_part

    first_part.next = second_part

    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("orignal list")
display(head)
print("")
print("After alteration")
reversed_lst = reverse_sub_list(head, 2, 4)
display(reversed_lst)
