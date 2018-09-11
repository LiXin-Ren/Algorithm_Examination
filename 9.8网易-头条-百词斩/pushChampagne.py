"""
倒香槟

输入：
第一行为两个整数n，m表示香槟塔的总层数和指令条数
第二行为n个整数ai，表示每层香槟塔的初始容量
第三行到第2+m行有两种输入，一种是"2 x v"表示往第x层倒入体积为v的香槟
   一种是"1 k"表示询问第k层当前有多少香槟

输出：
对每个询问，输出一个整数，表示第k层香槟的容量
"""
"""
1 2
8
2 1 9
1 1
"""

"""
5 4
1 2 2 10 1
1 3
2 2 5
2 4 3
1 4
"""
n, m = list(map(int, input().split()))
volumnMax = list(map(int, input().split()))     #每层的容量
nowVolumn = [volumnMax[i] for i in range(n)]                       #当前的容量
def pushS(que):
    x, v = que[1]-1, que[2]
    # if nowVolumn[x] > v:
    #     nowVolumn[x] -= v

    while x < n and v > nowVolumn[x]:
        v -= nowVolumn[x]
        nowVolumn[x] = 0
        x += 1
    if v != 0 and x < n:
        nowVolumn[x] -= v


for i in range(m):
    question = list(map(int, input().split()))
    if question[0] == 2:
        pushS(question)
    elif question[0] == 1:
        print(volumnMax[question[1]-1] - nowVolumn[question[1]-1])


