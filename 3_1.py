import re
N = 3
kor ='''
    1 5
    
    8 9
    3 7
  
    '''
res = "\d+\.?\d*"
def chunkIt(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

k = re.findall(res, kor)
for i in range(len(k)):
    k[i] = float(k[i])
k = chunkIt(k, N)
k = sorted(k) 
sum = 0
l = k[0][0]
r = k[0][1]
for i in range(N):
    if(i+1 < N):
        if k[i][1] < k[i+1][0]:
            sum += r-l 
            l = k[i+1][0]
            r = k[i+1][1]
        elif k[i][1] == k[i+1][0]:
            sum += r-l 
            l = k[i+1][0]
            r = k[i+1][1]
        else:
            if k[i][1] < k[i+1][1]:
                r = k[i+1][1]
            else:
                sum += r-l 
                l = k[i][1]
                r = k[i][1]
    else:
        if k[i][0] < l:
            sum += k[i][1] - l
        else:
            sum += k[i][1] - k[i][0]
            
    print(sum)
print(k)
print(sum)
