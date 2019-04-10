import re
N = 8
kor ='''
    1 11 5
    2 6 7
    3 13 9
    12 7 16
    14 3 25
    19 18 22
    23 13 29
    24 4 28
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
    k[i] = int(k[i])
k = chunkIt(k, N)
k = sorted(k) 
print(k)

output = []
h = []
l = []
r = []
#for i in k:
#    l.append(i[0])
#    h.append(i[1])
#    r.append(i[2])

for i in k:
    if len(h) == 0:
        l.append(i[0])
        h.append(i[1])
        r.append(i[2])
        output.append([i[0], i[1]])
    elif i[0] > max(l) or i[1] > max(h) or i[2] > max(r):
        
        if i[1] > max(h):
            output.append([i[0], i[1]])
        if i[0] > max(r):
            output.append([max(r), 0])
            h = []
            l = []
            r = []
        l.append(i[0])
        h.append(i[1])
        r.append(i[2])
        
        
      
            
     
print(output)     
                
