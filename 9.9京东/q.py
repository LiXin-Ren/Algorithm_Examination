

"""
对于仅由小写字母组成的字符串A和B，如果分别存在一个小写字母a到z的排列，
使得将A中所有字母a替换为排列的第一个字母，所有字母b替换为排列的第二个字母……所有字母z替换为排列的最后一个字母之后
，A和B完全相同，那么称字符串A和B相似，
如abcc和xyaa。现在给定仅由小写字母组成且长度不超过105的字符串S和T，求S中有多少子串与T相似？
"""


# def isMatch(str2):
#     strDict = {}
#     for ch in T:
#         if ch not in str2:
#             strDict[ch] = 1
#         else:
#             strDict[ch] += 1
#     strList = sorted(strDict.values())
#     return strList
#
#
# def Sover(S, T):
#     # T:子串
#     lenS = len(S)
#     lenT = len(T)
#     if lenS < lenT:
#         return False
#     TDict = {}
#     for ch in T:
#         if ch not in TDict:
#             TDict[ch] = 1
#         else:
#             TDict[ch] += 1
#     TList = sorted(TDict.values())
#     count = 0
#     for i in range(lenS-lenT):
#         if TList == isMatch(S[i:lenT+i]):
#             count += 1
#     return count
#
# S = input()
# T = input()
#
# print(Sover(S, T))

# !/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def str2list(aStr):
    strDict = {}
    for ch in aStr:
        if ch not in strDict:
            strDict[ch] = 1
        else:
            strDict[ch] += 1
    strList = sorted(strDict.values())
    return strList


def solve(S, T):
    lenS = len(S)
    lenT = len(T)
    if lenS < lenT:
        return 0

    TList = str2list(T)
    count = 0
    for i in range(lenS - lenT+1):
        if TList == str2list(S[i:lenT + i]):
            count += 1
    return count


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")
