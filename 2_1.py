import math 
import time 
st_time = time.time()
arr = []
str = "126+15*(36^25+{{7-15*3}*12+25/2+7*[123-78/5])"
state = 'Yes'
for i in str:
    if i == '(' or i == '{' or i == '[' or i == '<':
        arr.append(i)
    if i == ')' :
        if arr.pop() == '(':
            pass
        else:
            state = 'No'
    if i == '}':
        if arr.pop() == '{':
            pass
        else:
            state = 'No'
    if i == ']':
        if arr.pop() == '[':
            pass
        else:
            state = 'No'    
    if i == '>':
        if arr.pop() == '<':
            pass
        else:
            state = 'No'
if len(arr)!=0 :
    state = "No"
end_time = time.time()
tim = end_time - st_time
print("Время выполнения {} секунд".format(tim))
print (state)
