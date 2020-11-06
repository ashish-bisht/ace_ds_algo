def find_subsets(nums):
    subsets = []
    helper(nums, [], subsets)
    return subsets


def helper(nums, cur, subsets):
    if not nums:
        subsets.append(cur)
        return

    subsets.append(cur)

    for i in range(len(nums)):
        helper(nums[:i]+nums[i+1:], cur+[nums[i]], subsets)


print("Here is the list of subsets: " + str(find_subsets([1, 3])))
print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
