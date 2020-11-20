def can_partition(nums):
    total = sum(nums)

    return helper(nums, total//2) if total % 2 == 0 else False


def helper(nums, sum):
    row_length = len(nums)+1
    col_length = sum+1

    # create matrix
    matrix = [[False for _ in range(col_length)] for _ in range(row_length)]

    # intialisation
    for row in range(row_length):
        matrix[row][0] = True

    # Main Logic
    for row in range(1, row_length):
        for col in range(1, col_length):

            # if without adding we can get sum to awseome.
            if matrix[row-1][col]:
                matrix[row][col] = True
            elif col >= nums[row-1]:
                matrix[row][col] = matrix[row-1][col-nums[row-1]]
            # no need of else as we have already set everthing to false...
    return matrix[-1][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
