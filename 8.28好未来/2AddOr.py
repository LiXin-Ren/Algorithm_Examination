"""
一个等式x+y=x|y("|"表示或运算)，给出一个正整数x，满足等式的正整数y有很多个，从第一个开始由小到大数y，
给定一个正整数k求第k个y

输入：
t表示有t组数据(t<100)
每组数据输入x和k(0<x<10^18, 0<k<10^18)

输出：
y

示例：
input:
1
4 2

output:
2
思路：
以二进制的形式表示，例如4=100, 所有满足条件的y，只有一个限制，那就是第三位一定为0.
所以如果k=5，转为二进制101，将101填充到100上面，填充的规则是若x的位上为0，那么跟k一致，若x的位为1，
结果位为0，且n位右移一位。
"""

def solution(x, k):
    y = 0
    power = 0
    while k > 0:
        if x % 2 == 0:
            y += pow(2, power)*(k % 2)
            x = x >> 1
            k = k >> 1
            power += 1
        else:
            power += 1
            x = x >> 1
    return y

t = int(input())        # 组数
res = []
for i in range(t):
    x, k = map(int, input().split())
    res.append(solution(x, k))
for i in res:
    print(i, end=" ")


