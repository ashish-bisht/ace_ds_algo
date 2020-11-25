board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "SEE"

board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "ABCB"


def word_search(matrix, word):

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if dfs(matrix, row, col, word):
                return True

    return False


def dfs(matrix, row, col, word):
    if len(word) == 0:
        return True

    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or word[0] != matrix[row][col]:
        return False

    temp = matrix[row][col]
    matrix[row][col] = "#"

    up = dfs(matrix, row-1, col, word[1:])
    down = dfs(matrix, row+1, col, word[1:])
    left = dfs(matrix, row, col-1, word[1:])
    right = dfs(matrix, row, col+1, word[1:])
    res = up or down or left or right
    matrix[row][col] = temp

    return res


print(word_search(board, word))
print(word_search(board1, word1))
print(word_search(board2, word2))
