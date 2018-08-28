"""
使用方法：KMP
判断是不是双生词
1.S与S'长度相同
2.将S首尾相接绕成环，再选一个位置切开，顺时针或逆时针能够得到S'
给定一批仅由英文小写字母组成的字符串，询问他们之中是否存在双生词
input：
首先给出测试组数t，表示一共有多少组数据
对于每组数据，第一行为一个整数n，表示一共有多少个字符串。接下来n行，每行一个字符串
output：
对于每组数据，若存在双生词，输出Yeah。若不存在，输出Sad

示例：
3
2
helloworld
hdlrowolle
2
helloworld
worldhello
2
abcde
acbde

output:
Yeah
Yeah
Sad

1
2
helloworld
worldhello
"""
def next(p):
    # m为p的长度
    m = len(p)
    nextList = [-1] * m
    for i in range(1, m):
        k = nextList[i-1]
        while k != -1 and p[i] != p[k]:
            k = nextList[k]
        nextList[i] = k + 1
    return nextList

def kmp(s, p):
    s = s+s
    nextP = next(p)

    i = 0
    j = 0
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = nextP[j]
    if j == len(p):
        return True
    return False


def isTwinsWords(wordsList, numWords):
    for i in range(numWords):
        for j in range(numWords):
            if (i != j) and (len(wordsList[i]) == len(wordsList[j])):
                if kmp(wordsList[i], wordsList[j]) or kmp(wordsList[i], wordsList[j][::-1]):
                    return 'Yean'
    return 'Sad'

t = int(input())
res = []
for i in range(t):
    n = int(input())
    words = []                      #第i组词
    for j in range(n):
        words.append(input())
    res.append(isTwinsWords(words, n))
print(res)





