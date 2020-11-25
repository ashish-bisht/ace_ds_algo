matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


def spiral_matrix(matrix):
    row_start = 0
    row_end = len(matrix) - 1

    col_start = 0
    col_end = len(matrix[0]) - 1
    res = []
    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end):
            res.append(matrix[row_start][col])
        row_start += 1

        for row in range(row_start, row_end):
            res.append(matrix[row][col_end])
        col_end -= 1

        for col in reversed(range(row_start, row_end)):
            res.append(matrix[row_end][col])
        row_end -= 1

        for row in reversed(range(row_start, row_end)):
            res.append(matrix[row][col_start])
        col_start += 1

    return matrix


print(spiral_matrix(matrix))
