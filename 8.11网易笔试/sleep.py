"""
瞌睡问题：
输入：
第一行n、k：这堂课持续时间，以及叫醒小易一次使他能保持清醒的时间
第二行n个数：表示小易对每分钟知识点的感兴趣评分
第三行n个数：表示没分钟小易是否清醒，1表示清醒

输出：小易这堂课能听到的知识点最大的兴趣值

示例
input：
6 3
1 3 5 2 5 4
1 1 0 1 0 0
output:
16

用了滑动窗口的方式
"""

def mainFunction():
    nk = list(map(int, input().split()))
    n = nk[0]
    k = nk[1]

    values = list(map(int, input().split()))
    awake = list(map(int, input().split()))


    # for i in range(n):
    #     now += values[i] * awake[i]
    #计算清醒总时间
    awakeTime = sum(list(map(lambda x: x[0]*x[1], zip(awake, values))))
    #获取一个列表，这个列表将睡觉时的兴趣值记录下来，清醒时为0
    sleep = list(map(lambda x: (not x[0])*x[1], zip(awake, values)))
    max = 0
    #滑动窗口的方式记录最大值
    for i in range(n-k+1):
        if sum(sleep[i: i+k]) > max:
            max = sum(sleep[i: i+k])
    return awakeTime + max

print(mainFunction())