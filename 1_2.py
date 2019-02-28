import numpy as np
import time


def get_next_arr(arr):
    new_len = arr.size + 9

    new_arr = np.array([])
    for i in range(new_len):
        tmp = 0
        for j in range(10):
            if(i-j >= 0 and i-j < arr.size):
                tmp += arr[i-j]
        if(tmp != 0):
            new_arr = np.append(new_arr, tmp)

    return new_arr

def coun_num(num):
    arr = np.ones(10)
    if num > 1:
        for i in range(num-1):
            arr = get_next_arr(arr)
    arr = arr**2
    return int(arr.sum())




if __name__ == "__main__":
    number = int(input("Введите количество цыфр\n"))
    if (number % 2 == 0):
        st_time = time.time()
        number = int(number/2) 
        print("Число счастливых билетов {}".format(coun_num(number)))
        print("время выполнения \n--- %s seconds ---" % (time.time() - st_time))

    else:
        print("Число не являеться парным")