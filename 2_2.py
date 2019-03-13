#python 3.5.2
import re
#3 
str = "2.0+2.0*2-(2/2+2)" 


res = "\d+\.?\d*"
res_sim = "[\+\-\*\/\(\)]{1}"

num = re.findall(res, str)
sim = re.findall(res_sim, str)
print (num)
