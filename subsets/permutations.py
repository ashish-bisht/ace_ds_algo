def find_permutations(nums):
    length = len(nums)
    result = []
    helper(nums, [], result, length)
    return result


def helper(nums, cur, result, length):
    if len(cur) == length:
        result.append(cur)
        return

    for i in range(len(nums)):
        helper(nums[:i]+nums[i+1:], cur + [nums[i]], result, length)


print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
