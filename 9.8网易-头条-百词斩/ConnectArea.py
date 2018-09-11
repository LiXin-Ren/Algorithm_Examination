"""
连通域个数 （4联通）
输入：
第一行一个整数，代表矩阵大小M
后面M行，每行M个整数（取值为0或1）

输出：
一个整数，表示部门数量

示例：
input：
5
1 0 0 1 1
1 0 0 1 1
0 0 1 0 0
0 0 1 0 0
0 0 1 0 0

output：3

通过80%
"""
def solve(row, col, array):
    if array[row][col] == 0:
        return 0

    array[row][col] = 0
    if row + 1 < len(array):
        solve(row + 1, col, array)
    if col + 1 < len(array[0]):
        solve(row, col+1, array)
    if row - 1 >= 0:
        solve(row-1, col, array)
    if col - 1 >= 0:
        solve(row, col - 1, array)

    return



def main(M, array):
    countNum = 0

    for i in range(M):
        for j in range(M):
            if array[i][j] == 1:
                solve(i, j, array)
                countNum += 1
    return countNum

M = int(input())
array = []
for i in range(M):
    line = list(map(int, input().split()))
    array.append(line)

print(main(M, array))

