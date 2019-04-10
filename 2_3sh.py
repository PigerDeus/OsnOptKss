
N =5
M =4

def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())
A = [i for i in range(1,N+1)]



print(A)
while(len(A)>1):
    print(A)
    shift(A, M*(-1)+1)
    del A[0]
print(A)
