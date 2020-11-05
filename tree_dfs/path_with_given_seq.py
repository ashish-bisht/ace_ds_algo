class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return helper(root, sequence, [])


def helper(root, sequence, cur):
    if not root:
        return sequence == cur

    if not root.left and not root.right:
        cur = cur + [root.val]
        return cur == sequence

    return helper(root.left, sequence, cur+[root.val]) or helper(root.right, sequence, cur+[root.val])


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)

print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
print("Tree has path sequence: " + str(find_path(root, [1, 1, 5])))
print("Tree has path sequence: " + str(find_path(root, [1, 6, 1])))
