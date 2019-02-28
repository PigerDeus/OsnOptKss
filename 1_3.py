import time


b = 1
t = 0
data = []


with open("input.txt") as f:
    for line in f:
        data.append([float(x) for x in line.split()])
N, k = data[0]

st_time = time.time()


while(N > 0):
    N -=b
    t +=1
    if (b < k):
        b +=1

end_time = time.time()

with open("output.txt", "w") as file:
    print(t, file=file)

tim = end_time - st_time
print("Время выполнения {}".format(tim))