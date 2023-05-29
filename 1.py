def func_task1(cage):
    for i in range(3):
        if cage[i][0] == cage[i][1] == cage[i][2] and cage[i][0] != ' ':
            return cage[i][0]
    for j in range(3):
        if cage[0][j] == cage[1][j] == cage[2][j] and cage[0][j] != ' ':
            return cage[0][j]
    if cage[0][0] == cage[1][1] == cage[2][2] and cage[0][0] != ' ':
        return cage[0][0]
    if cage[0][2] == cage[1][1] == cage[2][0] and cage[0][2] != ' ':
        return cage[0][2]
    return "Ничья"

cage = [
    ['X', 'X', 'X'],
    ['O', 'X', 'O'],
    ['O', 'X', 'O']
]

print(func_task1(cage), "победили")
