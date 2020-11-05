class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    res = []
    helper(root, 0, res)
    return sum(res)


def helper(root, cur, res):
    if not root:
        return 0

    if not root.left and not root.right:
        cur = cur*10+root.val
        res.append(cur)
    helper(root.left, cur*10+root.val, res)
    helper(root.right, cur*10+root.val, res)


root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
