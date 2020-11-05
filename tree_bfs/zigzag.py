
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def level_order_zigzag(root):
    level = [root]
    res = []

    while level:
        next_level = []
        cur_level_nodes = []

        for node in level:
            cur_level_nodes.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
        res.append(cur_level_nodes)

    i = 0
    while i < len(res):
        if i %2 != 0:
            res[i] = res[i][::-1]
        i+=1
    return res



root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)    
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print("Level order zigzag traversal: " + str(level_order_zigzag(root)))
