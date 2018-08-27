"""
input:
12,15
16,17
12,20
-1,-1
output:
"""
def main():
    time = [0 for i in range(8)]
    while True:
        timeLine = list(map(int, input().split(',')))
        if timeLine[0] == -1:
            break
        for i in range(timeLine[0]-12, timeLine[1] - 12):
            time[i] += 1
    return time

res = main()
for i in range(8):
    print('['+str(i+12)+','+str(i+13)+']:'+str(res[i]))


