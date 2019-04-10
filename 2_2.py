import re
import operator

str = "2+2*2-(2/2+2)" 
OPERATORS = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
operator_pow = {'+':1, '-':1, '*':2, '/':2}

ar_stk = []
stk = []
stk_op = []
output = []
tmp = ''
res = "\d+\.?\d*"
res_sim = "[\+\-\*\/\(\)]{1}"
al = "(\d+\.?\d*)?([\+\-\*\/\(\)]{1})?"
def doTrans():
    for i in clean_full:
        if i == '+' or i == '-':
            gotOper(i, 1)
        elif i == '*' or i == '/':
            gotOper(i, 2)
        elif i == '(':
            stk.append(i)
        elif i == ')':
            gotParent(i)
        else:
            output.append(i)
    for i in stk:
        output.append(i)
    # return output

def gotParent(ch):
    while(len(stk)> 0):
        chx = stk.pop()
        if (chx == '('):
            break
        else:
            output.append(chx)

def gotOper(opThis, prec1):
    while(len(stk)>0):
        opTop = stk.pop()
        if opTop == '(':
            stk.append(opTop)
            break
        else:
            prec2 = 0
            if opTop == '+' or opTop == '-':
                prec2 = 1
            else:
                prec2 = 2
            if prec2 < prec1:
                stk.append(opTop)
                break
            else:
                output.append(opTop)
    stk.append(opThis)
        
num = re.findall(res, str)
sim = re.findall(res_sim, str)
ful_ar = re.findall(al, str)
clean_full = []

for i in ful_ar:
    for j in i:
        if j != '':
            clean_full.append(j)
def doParse():
    for i in output:
        if i in OPERATORS:
            op2, op1 = float(ar_stk.pop()), float(ar_stk.pop())
            ar_stk.append(OPERATORS[i](op1,op2))
        else:
            ar_stk.append(i)
doTrans()
doParse()
print(output)

print(clean_full)
print(ar_stk)
