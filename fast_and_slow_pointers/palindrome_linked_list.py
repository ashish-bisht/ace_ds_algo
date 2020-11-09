class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    cur = head
    prev = None

    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev


def is_palindromic_linked_list(head):
    # first get the mid point

    if not head:
        return True

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow)

    copy_head_second_half = head_second_half

    # compare values

    while head and head_second_half:
        # print(head.val, head_second_half.val)
        if head.val != head_second_half.val:
            return False
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half)
    return True


head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

print("Is palindrome: " + str(is_palindromic_linked_list(head)))

head.next.next.next.next.next = Node(2)
print("Is palindrome: " + str(is_palindromic_linked_list(head)))
