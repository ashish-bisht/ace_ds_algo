def min_del_ins(s1, s2):
    row_len = len(s1)+1
    col_len = len(s2)+1
    ans = 0
    # create matrix..

    matrix = [[0 for _ in range(col_len)] for _ in range(row_len)]

    # Already intialisesd to zero

    for row in range(row_len):
        for col in range(col_len):
            if s1[row-1] == s2[col-1]:
                matrix[row][col] = 1+matrix[row-1][col-1]

            else:
                matrix[row][col] = max(matrix[row-1][col], matrix[row][col-1])
    print(matrix[-1][-1])
    return len(s1) + len(s2) - matrix[-1][-1] - matrix[-1][-1]


def main():
    print(min_del_ins("abc", "fbc"))
    print(min_del_ins("abdca", "cbda"))
    print(min_del_ins("passport", "ppsspt"))


main()
