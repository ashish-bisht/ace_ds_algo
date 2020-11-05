class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
    level = [root]
    res = 0

    while level:
        next_level = []
        for node in level:
            if not node.left and node.right:
                return res
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        res +=1
        level = next_level
        
    return res



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
root.left.left = TreeNode(9)
root.right.left.left = TreeNode(11)
print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
