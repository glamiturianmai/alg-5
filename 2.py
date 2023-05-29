def func_task2(matr, element):
    i = 0 #строки
    j = len(matr[0]) - 1 #столбцы
    while j < len(matr) and j >= 0:
        if matr[i][j] == element:
            return True
            print(matr[i][j])
        elif matr[i][j] > element: # может быть только слева
            j -= 1
            print(matr[i][j])
        else: # может быть только ниже
            i += 1
            print(matr[i][j])
    return False

matr= [
    [1, 8, 16],
    [3, 9, 26],
    [5, 38, 39]
]

element = 9
if func_task2(matr, element):
    print('элемент', element, "есть в матрице")
else:
    print('такого элемента', element, "нет в матрице")
