import math 
with open('input.txt') as f:
    N, r = [float(x) for x in next(f).split()] # read first line
    arr = []
    for line in f: # read rest of lines
        arr.append([float(x) for x in line.split()])
# [[0.0, 0.0], [2.0, 0.0], [2.0, 2.0], [0.0, 2.0]]
# print(arr)

sum = 0
f_x = 0
f_y = 0
s_x = 0
s_y = 0
for i in range(int(N)):
    # print (arr[i])
    # print (arr[i-1][0])
    # print (arr[i][1])
    sum += ((arr[i-1][0]-arr[i][0])**2 + (arr[i][1]-arr[i-1][1])**2)**0.5
    f_x = arr[i-1][0] - arr[i][0]
    s_x = arr[i-1][1] - arr[i][1]
    if (i + 1 == int(N)):
        f_y = arr[0][0] - arr[i][0]
        s_y = arr[0][1] - arr[i][1]
        
    else:
        f_y = arr[i+1][0] - arr[i][0]
        s_y = arr[i+1][1] - arr[i][1]
        
    arc_cos =math.acos((f_x * s_x) + (f_y * s_y) / (((f_x**2+f_y**2)**0.5) * ((s_x**2 + s_y**2)**0.5)))
   
    sum += arc_cos

    # math.acos
# sum += math.pi * 2 * r
print("Длина веревки {0:.2f}".format(sum))

with open("output.txt", "w") as file:
    print("{0:.2f}".format(sum), file=file)
