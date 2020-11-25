def set_matrix_zeroes(matrix):
    # go throw matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Now we will reverse our direction as our markers are very first ele..

    for row in reversed(range(len(matrix))):
        for col in reversed(range(len(matrix[0]))):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    return matrix


def main():
    print("Resulted matrix", set_matrix_zeroes(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print("Resulted matrix", set_matrix_zeroes(
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))


main()
