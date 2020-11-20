def edit_distance(s1, s2):

    row_len = len(s1) + 1
    col_len = len(s2)+1

    # create 2d matrix...

    matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    # intialisation is  done to len of other str..

    for row in range(row_len):
        matrix[row][0] = row

    for col in range(col_len):
        matrix[0][col] = col

    for row in range(1, row_len):
        for col in range(1, col_len):
            if s1[row-1] == s2[col-1]:
                # as nothing needs to be done
                matrix[row][col] = matrix[row-1][col-1]

            else:
                matrix[row][col] = 1 + \
                    min(matrix[row-1][col-1], matrix[row-1]
                        [col], matrix[row][col-1])

    return matrix[-1][-1]


print(edit_distance("bat", "but"))
print(edit_distance("abdca", "cbda"))
print(edit_distance("passpot", "ppsspqrt"))
