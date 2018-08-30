"""
listR的含义是存储余数第一次出现的时候
eg 1/7 = 0.14285714...
listR = [-1, -1, -1, -1, -1, -1]代表了[0, 1, 2, 3, 4, 5, 6](7的可能余数）

n = 0
0. 1%7 = 1，这是listR[1] = 0 #第一个1代表余数为1，说明有余数为1的情况了。0代表这是第0次求余时出现了余数为1
1. 1*10 % 7 = 3，这时listR[3] = 1 #第1次求余，余数为3
2. 3*10 % 7 = 2， listR[2] = 2  #第2次求余，余数为2
3. 2*10 % 7 = 6， listR[6] = 3 #第3次求余，余数为6
...
一直到余数遇到重复的了
"""
x, y = map(int, input().split())
x = x % y
n = 0
firstAppear = 0
length = 0
listR = [-1 for i in range(x)]
while True:
    if x == 0:
        firstAppear = n
        length = 0
        break
    if listR[x] != -1:
        firstAppear = listR[x]
        length = n - firstAppear
        break
    listR[x] = n
    n += 1
    x = (x * 10) % y

print(firstAppear, length)