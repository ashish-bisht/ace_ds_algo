
class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

## Algorithm...
## 1. Find length of 

def find_cycle_start(head):



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
