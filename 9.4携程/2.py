# import math
# p = list(map(int, input().split()))
# q = list(map(int, input().split()))
# KL = 0.0
# pPro = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# qPro = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
# for x in p:
#     pPro[x] += 1
# for y in q:
#     qPro[y] += 1
#
#
# for i in range(6):
#     KL += pPro[i] * math.log((pPro[i] / qPro[i]), 2)
# print(round(KL, 2))

# from math import log
#
# n = int(input())
# pos = 0
# neg = 0
# value_x = []
# x_y = dict()
# list_y = [0, 1]
# for i in range(n):
#     row = input().strip().split(', ')
#     x = int(row[0])
#     y = int(row[1])
#     if(y == 1):
#         pos += 1
#     if(y == 0):
#         neg += 1
#     if(x not in value_x):
#         value_x.append(x)
#         x_y[x] = dict()
#         x_y[x] = x_y[x].fromkeys(list_y, 0)
#
#     x_y[x][y] += 1
#
# print("x_y:\n", x_y)
# ES = 0
# if(pos != 0):
#     ES += - (pos / n) * log(pos / n, 2)
# if(neg != 0):
#     ES += - (neg / n) * log(neg / n, 2)
#
# XES = 0
# for xi in value_x:
#     n_xi = x_y[xi][0] + x_y[xi][1]
#     xes = 0
#     if(x_y[xi][0] != 0):
#         xes += -(x_y[xi][0]/n_xi) * log(x_y[xi][0]/n_xi, 2)
#     if(x_y[xi][1] != 0):
#         xes += -(x_y[xi][1]/n_xi) * log(x_y[xi][1]/n_xi, 2)
#     XES += xes
#
# print(ES-XES)