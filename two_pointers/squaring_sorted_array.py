def make_squares(arr):
    squares = [0 for i in range(len(arr))]
    left = 0
    right = len(arr)-1
    highest_square_index = len(arr)-1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1

        highest_square_index -= 1
    return squares


print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))
