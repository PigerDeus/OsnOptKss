
N =5
M = 3
L = 4
def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())

            
A = [i for i in range(1,N+1)]

k = ((N-1)*M)%N
shift(A, -k)
print("Отчёт начат с ")
print(A[L-1])
