class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):

    return helper(root, 0)


def helper(root, cur):
    if not root:
        return 0

    if not root.left and not root.right:
        return cur*10+root.val

    return helper(root.left, cur*10+root.val) + helper(root.right, cur*10+root.val)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
