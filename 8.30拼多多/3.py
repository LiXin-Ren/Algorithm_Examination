x, y = map(int, input().split())
x = x % y
n = 0
startIndex = 0
length = 0
listR = [-1 for i in range(1000000)]
while True:
    if x == 0:
        startIndex = n
        length = 0
        break
    if listR[x] != -1:
        startIndex = listR[x]
        length = n - startIndex
        break
    listR[x] = n
    n += 1
    x = (x * 10) % y

print(startIndex, length)