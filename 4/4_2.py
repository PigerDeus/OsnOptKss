res = []
programs = {}
cost = {}
count = 0
values = {}
with open("input2.txt", "r") as file:
  count = int(file.readline())
  for i in range(count):
    tmp =  file.readline().strip().split(' ')
    if tmp != '':
      programs[tmp[0]] = tmp[2:]
      cost[tmp[0]] = tmp[1]



while len(res) < count:
  for key in programs.keys():
    if len(programs[key]) == 0 and key not in res:
        res.append(key)
        values[key] = float(cost[key])
    elif key not in res:
        # if count - len(res) == 1:
        #     res.append(key)
        st = 0
        for i in programs[key]:
            if i != '':
                if i not in res:
                    st +=1
                if st > 0:
                    break
            
        if st == 0 and key not in res:
            res.append(key)
            tmp = 0
            for i in range(len(programs[key])):
                if tmp < (values[programs[key][i]]):
                    tmp = float(values[programs[key][i]])

                
            values[key] = tmp + float(cost[key])

max_t = 0
for i in values:
    if max_t < values[i]:
        max_t = values[i]
max_t = round(max_t, 1)
# print(max_t)
with open("output2.txt", "w") as file:
    
    print(max_t, file=file)
# print(programs)
# print(res)


