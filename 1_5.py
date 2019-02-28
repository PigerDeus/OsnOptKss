import math 
with open('input.txt') as f:
    N, r = [float(x) for x in next(f).split()] # read first line
    arr = []
    for line in f: # read rest of lines
        arr.append([float(x) for x in line.split()])
# print(arr)

sum = 0

for i in range(int(N)):
    # print (arr[i])
    # print (arr[i-1][0])
    # print (arr[i][1])
    sum += ((arr[i-1][0]-arr[i][0])**2 + (arr[i][1]-arr[i-1][1])**2)**0.5

sum += math.pi * 2 * r
print("Длина вер]вки {0:.2f}".format(sum))