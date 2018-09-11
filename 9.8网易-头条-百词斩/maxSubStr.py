"""
对子串进行翻转0次或多次 ，翻转方法：
把子串从某个地方切割开，将两个得到的子串同时翻转，然后拼接在一起
找出最长的黑白相间连续子串，

输入：一个字符串s，只包含'b'和'w'，分别表示黑色和白色

输出：
一个整数，表示改变之后最长的连续黑白相间的字串长度
"""

aStr = input()
aStr = aStr + aStr
def maxSubStr(aStr):
    maxLen = 1
    i = 0
    while True:
        temp = 1
        while i+1 < len(aStr) and aStr[i] != aStr[i + 1]:
            temp += 1
            i += 1
        if maxLen < temp:
            maxLen = temp
        if i+1>=len(aStr):
            break
        i+=1
    if maxLen > len(aStr)//2:
        return len(aStr) // 2
    else:
        return maxLen


print(maxSubStr(aStr))