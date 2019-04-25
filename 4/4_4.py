arr = []
dots = set()
res = []
dot = set()
current_dot = []
sum = 0
cost = []
with open("input4.txt") as f:
    line = f.readline()
    for i in range(int(line)):
        tmp = f.readline().strip().split(' ')
        dots.add(int(tmp[0]))
        dots.add(int(tmp[1]))
        arr.append([int(tmp[2]), int(tmp[1]), int(tmp[0])])
n = len(dots) - 1

arr = sorted(arr)
while len(res) < n:
    for i in arr:
        if len(res) == 0:
            dot.add(i[2])
            dot.add(i[1])
            sum += int(i[0])
            res.append([i[2],i[1]])
        elif i[2] in dot and i[1] not in dot:
            cost.append(i[0])
            current_dot.append([[i[2],i[1]]])
        elif i[1] in dot and i[2] not in dot:
            cost.append(i[0])
            current_dot.append([[i[2],i[1]]])
    tmp = cost.index(min(cost))
    sum += int(min(cost))
    res.append(current_dot[tmp][0])
    print(current_dot[tmp])
    dot.add(current_dot[tmp][0][0])
    dot.add(current_dot[tmp][0][1])
    current_dot = []
    cost = []
res = sorted(res)
print(res)
print(sum)
with open("output4.txt", "w") as file:
    for i in res:
        print("{} {} \n".format(i[0], i[1]), file=file)
    print(sum, file=file)