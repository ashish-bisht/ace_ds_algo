def rod_cutting(lengths, prices, n):

    row_length = len(lengths)+1
    col_length = n+1
    matrix = [[0 for _ in range(col_length)] for _ in range(row_length)]

    # Intialisation is not required as at 0 it will zero always...

    # logic
    for row in range(row_length):
        for col in range(col_length):
            if col >= lengths[row-1]:
                matrix[row][col] = max(
                    matrix[row-1][col], prices[row-1] + matrix[row][col - lengths[row-1]])
            else:
                matrix[row][col] = matrix[row-1][col]

    return matrix[-1][-1]


def main():
    print(rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
