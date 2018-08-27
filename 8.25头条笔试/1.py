
n = int(input())
res = [0 for i in range(n)]
currentNum = 1
for i in range(n):
    line = list(map(int, input().split()))
    if res[i] == 0:
        iNum = currentNum
        for num in line:
            if num != 0 and res[num - 1] != 0 and res[num - 1] <iNum:
                iNum = res[num - 1]
        res[i] = iNum
        if iNum == currentNum:
            currentNum += 1
    else:
        iNum = res[i]
        for num in line:
            if num != 0 and res[num - 1] != 0 and res[num - 1] <iNum:
                iNum = res[num - 1]
        res[i] = iNum

    for num in line:
        if num != 0:
            res[num - 1] = iNum


print(max(res))
#print(max(currentNum))