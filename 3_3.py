import sys, array, tempfile, heapq
assert array.array('i').itemsize == 4

iters = []
open('output.txt', 'w').close()
f_input = open('input.txt', 'r')
d = f_input.readline()
def intsfromfile(name):
    f_temp = open(name, 'r')
    while True:
        a=[]
        for ii in range(0,100000):
            line = f_temp.readline()
            if line != '':
              a.append(float(str(line).strip()))
        if not a:
             break
        for x in a:
             yield x
    f_temp.close()

iii=0
while True:
  a=[]
  for ii in range(0,100000):
    line = f_input.readline()
    if line != '':
      a.append(float(str(line).strip()))
  if not a:
      break
  f_name = 'tempfile%d' % iii    
  f_temp = open(f_name, 'a')
  iii +=1
  b = sorted(a)
  for yy in b:
    f_temp.write(str(yy)+'\n')
  f_temp.close()
  iters.append(intsfromfile(f_name))


f_output = open('output.txt', 'a')
for x in heapq.merge(*iters):
  f_output.write(str(x)+'\n')
f_output.close()
