def count_subsets(nums, sum):

    row_length = len(nums)+1
    col_length = sum+1

    # create matrix....
    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    # intialiase...
    for row in range(row_length):
        matrix[row][0] = 1

    # Final Code..

    for row in range(1, row_length):
        for col in range(1, col_length):
            if col >= nums[row-1]:
                matrix[row][col] = matrix[row-1][col] + \
                    matrix[row-1][col - nums[row-1]]
            else:
                matrix[row][col] = matrix[row-1][col]

    return matrix[-1][-1]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))


main()
