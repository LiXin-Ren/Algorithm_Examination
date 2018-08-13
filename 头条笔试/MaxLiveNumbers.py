"""
input:
3
10
0 5 2 7 6 9
ouput: 2

input:
3
10
0 3 3 7 7 0
output:3
"""
n = int(input())
hours = int(input())

timeLine = list(map(int, input().split()))
timeStamp = []
for i in range(len(timeLine)):
    if i % 2 != 0:
        timeStamp.append([timeLine[i-1], timeLine[i]])

for i in range(1, len(timeStamp)):
    if timeStamp[i][1] == 0:
        timeStamp[i][1] = hours
timeStamp.sort(key=lambda x: x[0])          #a按起始时间排序

num = 0
tmp = [0, 0]    #当前正在看的
for time in timeStamp:
    if time[0] >= tmp[1]:                   #如果下一个起始时间大于等于当前的终止时间。那么相当于把当前的看完了
        num += 1
        tmp = time
    else:
        if time[1] < tmp[1]:                #如果下一个终止时间小于当前终止时间，那么转看下一个。
            tmp = time
print(num)

