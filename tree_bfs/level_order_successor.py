
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def find_successor(root, key):
    level = [root]
    values = []
    res = float("inf")

    while level:
        next_level = []

        for node in level:
            values.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    i = 0
    while i < len(values):
        if values[i] == key:
            if values[i+1]:
                return values[i+1]
                break 
        i +=1
    return res



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)

print(find_successor(root, 12))
print(find_successor(root,9))


