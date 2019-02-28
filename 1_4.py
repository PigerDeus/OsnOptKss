import time

data = []
with open("input.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])
st_time = time.time()

a = data[0]

N = a[0]
sum=0
a = 0
p = 0
while sum != N:
    sum += a + p
    p +=1
    if (sum > N):
        sum = 0
        a +=1
        p = 0

res =  str(a) + " " + str(p)

end_time = time.time()
tim = end_time - st_time
print("Время выполнения {} секунд".format(tim))


with open("output.txt", "w") as file:
    print(res, file=file)