def long_com_substring(s1, s2):

    row_len = len(s1)+1
    col_len = len(s2) + 1

    # create matrix

    matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    # Already intialisesd to zero
    max_string = 0
    # Main logic
    for row in range(1, row_len):
        for col in range(1, col_len):
            if s1[row-1] == s2[col-1]:
                matrix[row][col] = matrix[row-1][col-1] + 1

            max_string = max(max_string, matrix[row][col])

    return max_string


def main():
    print(long_com_substring("abdca", "cbda"))
    print(long_com_substring("passport", "ppsspt"))


main()
