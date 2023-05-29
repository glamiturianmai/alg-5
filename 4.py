def func_task4(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    list = [0] * (n+1)
    list[0] = 1
    list[1] = 1
    list[2] = 2

    for i in range(3, n+1):
        list[i] = list[i-1] + list[i-2] + list[i-3]
    return list[n]

n = 3
print("Количество вариантов для лестницы из", n, "ступенек:", func_task4(n))