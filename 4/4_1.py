res = []
programs = {}
count = 0
with open("input.txt", "r") as file:
  count = int(file.readline())
  for i in range(count):
    tmp =  file.readline().strip().split(' ')
    if tmp != '':
      programs[tmp[0]] = tmp[1:]

while len(res) < count:
  for key in programs.keys():
    if len(programs[key]) == 0 and key not in res:
        res.append(key.strip())

    elif key not in res:
        if count - len(res) == 1:
            res.append(key)
        st = 0
        for i in programs[key]:
            if i != '':
                if i not in res:
                    st +=1
                if st > 0:
                    break
        if st == 0 and key not in res:
            res.append(key)

    
with open("output.txt", "w") as file:
    for i in res:
        print("{}  ".format(i), file=file)
  

print(res)
    
