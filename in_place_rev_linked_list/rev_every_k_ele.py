class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def display(head):
    while head:
        print(head.value, end=" ")
        head = head.next


def reverse_every_k_elements(head, k):

    # def reverseKGroup(self, head, k):
    #     count, node = 0, head
    #     while node and count < k:
    #         node = node.next
    #         count += 1
    #     if count < k:
    #         return head
    #     new_head, prev = self.reverse(head, count)
    #     head.next = self.reverseKGroup(new_head, k)
    #     return prev

    # def reverse(self, head, count):
    #     prev, cur, nxt = None, head, head
    #     while count > 0:
    #         nxt = cur.next
    #         cur.next = prev
    #         prev = cur
    #         cur = nxt
    #         count -= 1
    #     return (cur, prev)


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

print("Nodes of original LinkedList are: ", end='')
display(head)
result = reverse_every_k_elements(head, 3)
print("Nodes of reversed LinkedList are: ", end='')
display(result)
