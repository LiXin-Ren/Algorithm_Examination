"""
矩阵立起来后的状态
3 4
.oxo
o..o
.xox
....
"""

n, m = map(int, input().split())

matrixRaw = []
for i in range(n):
    s = input()
    matrixRaw.append(s)     #一个列表存储

flag = [[None, None] for i in range(m)]          #最近的一个障碍物位置
for i in range(n-1 , -1, -1):   #从最后一行遍历
    for j in range(m):
        if matrixRaw[i][j] == 'x':
            flag[j][0] = i         #当前列的障碍物位置
            flag[j][1] = i - 1
        elif matrixRaw[i][j] == 'o':
            matrixRaw[i] = matrixRaw[i][:j] + '.' + matrixRaw[i][j+1:]
            if flag[j][0]:
                matrixRaw[flag[j][1]] = matrixRaw[flag[j][1]][:j] + 'o' + matrixRaw[flag[j][1]][j+1:]
                flag[j][1] -= 1
print('now')
for i in range(n):
    print(matrixRaw[i])


