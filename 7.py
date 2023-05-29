import random
def func_task7():
    list=[]
    k=0
    for i in range(random.randint(0, 100)):
        list.append(random.randint(0, 50))
    print(list)
    arr=[False]*(len(list)+1)
    for num in list:
        if num in list:
            if 0<= num <=len(list):
                arr[num]=True
    for i in range(1, len(list)+1):
        if not arr[i]:
            print("наименьшее пропущенное число", i)
            k=1
            break
    if k==0:
        print('наименьшее пропущенное число', len(list)+1)

func_task7()