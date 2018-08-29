"""
一个数字串可以被拆成多个数字串，例如12345拆成12 3 45或者123 45.给一个正整数类型的数字串n，求n拆开后的数
能被3整数的最大数量m是多少（0也算3的倍数）
12，3，45，m=3
123,45,m = 2

输入描述：
输入一个正整数类型的数字串n（字符串长度<100)
输出：一个数字表示n拆开后能被3整除最多的数量。

示例：
input:
321
output:
2

解题思路：
i = 0开始
若n[i] % 3 == 0,那么sum += 1，i += 1,判断下面的数
否则如果(n[i] + n[i+1]) % 3 == 0, sum += 1, i = i+2
如果(n[i] + n[i+1]) % 3 != 0, 那么sum += 1, i = i+3
关键信息在于，任何3个数组合，至少有一个能被3整除，可以从余数的角度考虑。
"""
s = input()
lengthS = len(s)
i = 0
totalNum = 0
while i < lengthS:
    if int(s[i]) % 3 == 0:
        totalNum += 1
        i += 1
    else:
        if i + 1 < lengthS:
            if (int(s[i+1]) % 3 == 0 or (int(s[i]) + int(s[i+1])) % 3 == 0):
                totalNum += 1
                i += 2
            elif i + 2 < lengthS:
                totalNum += 1
                i += 3
            else:
                break
        else:
            break
print(totalNum)
