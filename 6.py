alpha = 0.1 # должно быть меньше 1

def func_task6(value, new_value):
    return alpha * new_value + (1 - alpha) * value

print(func_task6(1, 10))