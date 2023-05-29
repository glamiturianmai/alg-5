def desk(board, row, col): #можем ли мы разместить ферзя так: доска, строка, столбец
    if any(board[row][i] == 1 for i in range(8)): #горизонтальная линия
        return False
    if any(board[i][col] == 1 for i in range(8)): #вертикальная линия
        return False
    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, -1, -1))) or any(board[i][j] == 1 for i, j in zip(range(row, 8), range(col, 8))): # главная диагональ
        return False
    if any(board[i][j] == 1 for i, j in zip(range(row, -1, -1), range(col, 8))) or any(board[i][j] == 1 for i, j in zip(range(row, 8), range(col, -1, -1))):# побочная диагональ
        return False
    return True


def func_task3(board, row):
    if row == 8:
        print(board)
        return True

    for col in range(8):
        if desk(board, row, col):
            board[row][col] = 1
            func_task3(board, row+1)
            board[row][col] = 0

    return False


board = [[0 for i in range(8)] for j in range(8)]
# Размещаем ферзей на доске
func_task3(board, 0)