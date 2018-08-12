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
















