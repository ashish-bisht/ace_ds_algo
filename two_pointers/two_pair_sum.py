def two_aum(nums, target):
    left, right = 0, len(nums)-1

    while left <= right:
        cur_num = nums[left] + nums[right]

        if cur_num == target:
            return [nums[left], nums[right]]

        if cur_num > target:
            right -= 1

        if cur_num < target:
            left += 1

    return [-1, -1]


print(two_aum([2, 7, 11, 15], 9))
