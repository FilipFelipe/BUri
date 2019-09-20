# -*- coding: utf-8 -*-

op = int(input())
x = []
y = []
for i in range(op):
    num = input().split()
    x.append(int(num[0]))
    y.append(int(num[1]))
for top in range(op):
    if y[top] == 0:
        print("divisao impossivel")
    else:
       print(x[top] / y[top])
