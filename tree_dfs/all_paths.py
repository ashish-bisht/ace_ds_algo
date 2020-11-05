class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def find_paths(root, sum):
    all_paths = []
    helper(root, sum, [], all_paths)
    return all_paths


def helper(root, sum, cur, all_paths):
    if not root:
        return
    if sum == root.val and not root.left and not root.right:
        all_paths.append(cur+[root.val])
        return

    helper(root.left, sum-root.val, cur+[root.val], all_paths)
    helper(root.right, sum-root.val, cur+[root.val], all_paths)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
sum = 23
print("Tree paths with sum " + str(sum) +
      ": " + str(find_paths(root, sum)))

# Answer  Tree paths with required_sum 23: [[12, 7, 4], [12, 1, 10]]
