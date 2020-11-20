def can_partition(nums, sum):

    # create 2 d matrix:::
    col_length = sum+1
    row_length = len(nums)+1
    matrix = [[False for _ in range(col_length)] for _ in range(row_length)]

    # Initialisation with base cobnditiond, ismein lun ya na lun ke ye number ban jaye....
    for row in range(row_length):
        matrix[row][0] = True

    # Now main loop, idhar check karna hai ke is particular ke sath ban sakta ke nahin, in short lun ya na lun...

    for row in range(1, row_length):
        for col in range(1, col_length):

            # phele check if we can have number without current one...
            if matrix[row-1][col]:
                matrix[row][col] = True

            elif col >= nums[row-1]:
                # abhi ka number - karke check if jo bacha hai wo result kya hai..
                matrix[row][col] = matrix[row-1][col - nums[row-1]]

    return matrix[-1][-1]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))


main()
