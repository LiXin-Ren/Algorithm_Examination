"""
给出N个长度都为L的单词，单词中仅包含大写英文字母（A-Z）
你可以从这些单词中的第一个字母中挑一个作为你拼词的第一个字母，所有单词的第二个字母中挑一个作为你拼词的第二个字母...
依次类推
比如给出N=3个L=4的单词：
CAKE
TORN
SHOW
你可以（但不限于）拼出以下单词：
CORN
SAKE
CHRE
问：按照上述规则拼出一个与输入的N个单词都不相同的单词，若无法频出，则输出“-”，
若超过一个符合条件的单词，则输出字典序最小的那一个。
数据范围：
1<=N<=2000
1<=L<=10

输入：
第一行包含2个整数N，L，
"""
n, l = map(int, input().split())
se = []
s = ['']*l
output = []

def dfs(now, output):
    if now == l:
        output = "".join(output)
        if se.count(output):    #查找se中是否存在output
            return False
        else:
            return True

    last = "#"
    for i in range(n):
        if last == s[now][i]:       # 避免重复搜索
            continue
        last = s[now][i]
        output.append(last)
        ok = dfs(now + 1, output)
        if ok:
            return True
    return False


for i in range(n):
    curr = input()
    se.append(curr)
    for j in range(l):
        s[j] += curr[j]

for i in range(l):
    s[i] = "".join(sorted(s[i]))
ok = dfs(0, output)
if ok:
    print('yes')
    print("".join(output))
else:
    print("-")

"""
3 4
COKE
TARN
SHOW
BBBB
"""