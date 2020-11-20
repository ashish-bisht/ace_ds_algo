def longest_common_subseq(s1, s2):

    # create matrix..
    row_length = len(s1) + 1
    col_length = len(s2) + 1

    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    # Initialisation is not needed as we have already made everything zero, and base case also make zeros

    # main logic

    for row in range(1, row_length):
        for col in range(1, col_length):
            if s1[row-1] == s2[col-1]:
                matrix[row][col] = 1 + matrix[row-1][col-1]

            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])

    return matrix[-1][-1]


def main():
    print(longest_common_subseq("abdca", "cbda"))
    print(longest_common_subseq("passport", "ppsspt"))


main()
