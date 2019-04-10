N = 5
M = 4

p = [i for i in range(1, N+1)]
i = 0
j = 1

while(len(p)> 1):
     print(j)
     print(p)
     i += 1
     if j + 1 >= len(p):
         j = 0  
     else:
         j +=1

     if i%M:
        del p[j]
     
print(p)