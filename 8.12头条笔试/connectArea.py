"""
相当于是一个求二值矩阵联通域的题。要求得出连通域个数和最大的连通域。
使用的方法是：
首先遍历数组，遇到一个“1”就将其标记为当前的flag值（flag从2开始）。
然后将1周围的8邻域遍历，寻找有没有值为“1”的，如果有，那么将其标记为flag，并调用search。
"""
"""
初始方法：
def isRoad(row, col, M, N):
    if row < M and row >=0 and col>= 0 and col < N:
        return True
    return False

def search(row, col, M, N,  array, flag, num):
    if isRoad(row+1, col, M, N) and array[row+1][col] == 1:
        array[row + 1][col] = flag
        num += 1
        num = search(row + 1, col, M, N, array, flag, num)
    if isRoad(row-1, col, M, N) and array[row-1][col] == 1:
        array[row - 1][col] = flag
        num += 1
        num = search(row - 1, col, M, N, array, flag, num)

    if isRoad(row, col-1, M, N) and array[row][col-1] == 1:
        array[row][col - 1] = flag
        num += 1
        num = search(row, col - 1, M, N, array, flag, num)
    if isRoad(row, col+1, M, N) and array[row][col+1] == 1:
        array[row][col + 1] = flag
        num += 1
        num = search(row, col + 1, M, N, array, flag, num)

    if isRoad(row+1, col+1, M, N) and array[row+1][col+1] == 1:
        array[row + 1][col + 1] = flag
        num += 1
        num = search(row + 1, col+1, M, N, array, flag, num)
    if isRoad(row+1, col-1, M, N) and array[row + 1][col-1] == 1:
        array[row + 1][col - 1] = flag
        num += 1
        num = search(row + 1, col - 1, M, N, array, flag, num)

    if isRoad(row-1, col+1, M, N) and array[row-1][col+1] == 1:
        array[row + 1][col + 1] = flag
        num += 1
        num = search(row - 1, col + 1, M, N, array, flag, num)
    if isRoad(row-1, col-1, M, N) and array[row-1][col-1] == 1:
        array[row + 1][col + 1] = flag
        num += 1
        num = search(row - 1, col - 1, M, N, array, flag, num)

    return num

def main(M, N, array):
    flag = 2
    count = []
    for i in range(M):
        for j in range(N):
            if array[i][j] == 1:
                num = 1
                array[i][j] = flag
                num = search(i, j, M, N, array, flag, num)
                count.append(num)
                flag += 1
    print(array)
    return count

M = 10
N = 10

matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

connects = main(M, N, matrix)
print("球队个数： ", len(connects))
print("数量最多的球队： ", max(connects))

"""
#改进方法：
def solve(row, col, array):
    if array[row][col] == 0:
        return 0
    count = 1
    array[row][col] = 0
    if row + 1 < len(array):
        count += solve(row + 1, col, array)
    if col + 1 < len(array[0]):
        count += solve(row, col+1, array)
    if row - 1 >= 0:
        count += solve(row-1, col, array)
    if col - 1 >= 0:
        count += solve(row, col - 1, array)

    if row - 1 >= 0 and col - 1 >= 0:
        count += solve(row - 1, col - 1, array)
    if row + 1 < len(array) and col + 1 < len(array[0]):
        count += solve(row + 1, col + 1, array)
    if row + 1 < len(array) and col - 1 >= 0:
        count += solve(row + 1, col - 1, array)
    if row - 1 >= 0 and col + 1 < len(array[0]):
        count += solve(row - 1, col + 1, array)
    return count


def main(M, N, array):
    countNum = 0
    maxCount = 0
    for i in range(M):
        for j in range(N):
            if array[i][j] == 1:
                count = solve(i, j, array)
                if count > maxCount:
                    maxCount = count
                countNum += 1
    return countNum, maxCount


M = 10
N = 10
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
]

num, numMax = main(M, N, matrix)
print("球队个数： ", num)
print("数量最多的球队： ", numMax)
















