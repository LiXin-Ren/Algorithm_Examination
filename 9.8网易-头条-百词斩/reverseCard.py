"""
给定一个N*M的矩阵，在矩阵中每一块有一张牌， 假定刚开始的时候所有的牌面向上。现在对于每一个块进行如下操作：
翻转某个块中的牌 ，并且与之相邻的其余八张牌也会被翻转。
XXX
XXX
XXX
如上矩阵所示，翻转中间的牌时，所有9张牌都会被翻转
请输出对矩阵中每一块进行如上操作时，牌面向下的块的个数
"""
"""
输入第一行为测试用例数t
接下来t行，每行包含两个整数N,M

输出仅包含一行，输出牌面向下的个数

示例：
input:
5
1 1
1 2
3 1
4 1
2 2

output:
1
0
1
2
0

"""
#
# def calculate(N, M):
#     xi = [1, 1, 0, -1, -1, -1, 0, 1]
#     yi = [0, -1, -1, -1, 0, 1, 1, 1]
#     #state = []
#     totalNum = 0
#     for i in range(N):
#         for j in range(M):
#             s = 0
#             for z in range(8):
#                 if (i + xi[z]) < N and (j + yi[z]) < M and (i + xi[z]) >= 0 and (j + yi[z]) >= 0:
#                     s += 1
#             s += 1
#             totalNum += s % 2
#
#     return totalNum


def calculate(N, M):
    if M == 1:
        if N == 1:
            return 1
        if N > 2:
            return N - 2
        return 0
    if M == 2:
        return 0
    else:
        return (N - 2)*(M-2)


t = int(input())
#counts = []
for i in range(t):
    N, M = list(map(int, input().strip().split()))
    if N < M:
        N, M = M, N             #N>M
    print(calculate(N, M))
    # count = calculate(N, M)
    # counts.append(count)

# for count in counts:
#     print(count)