"""
固定数组：{0,1, 2, 3, 4, 5, 6, 7, 8, 9}
输入布尔数组：{0, 1, 1, 1, 1, 1, 1, 1, 1, 0},其中0表示对于下标数组元素可出现也可以不出现，
1表示必须出现。输出所有可能性组合，转化为字符串，并按照字符串升序排序
排序：
012345678
0123456789
12345678
123456789

输入：位置出现的布尔值
输出：打印所有组合

示例：
input:
0 1 1 1 1 1 1 1 1 1 0

output:
012345678
0123456789
12345678
123456789
"""
basicList = [i for i in range(10)]
boolList = map(int, input().split())

def solution(aList):
    print()
    for i in range(10):
        if aList[i] == 0:
            temp = ''
            for k in range(0,i):
                temp += str(basicList[k])
            for t in range(i):


for i in range(10):
    if boolList[i] == 0:
        boolList[i] = 1
        solution(boolList)

sum0 = 10 - sum(boolList)       # 0的个数
for i in range(sum0):           # boolList[i] = 0
    newBool = boolList
    for j in range(i, 10):      # 余下的boolList
        if boolList =


