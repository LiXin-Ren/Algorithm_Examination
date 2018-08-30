
n, l = map(int, input().split())
se = []
s = ['']*l
output = ''

def dfs(now, output):
    if now == l:
        if se.count(output):    #查找se中是否存在output
            return False
        else:
            return True

    last = "#"
    for i in range(n):
        if last == s[now][i]:
            continue
        last = s[now][i]
        output += last
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
    print(output)
else:
    print("-")

"""
3 4
COKE
TARN
SHOW
BBBB
"""