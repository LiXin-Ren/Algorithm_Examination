
#
# def reverse(s):
#     neg = False
#     if s[0] == '-':
#         neg = True
#         s = s[1:]
#     s = s[::-1]
#     if neg:
#         return 0-int(s)
#     return int(s)
#
# s = input()
# print(reverse(s))
m, n = list(map(int, input().split()))
wordMap = []
for i in range(m):
    wordMap.append(input())

def searchOther(target, row, col):
    if target == '':
        return True
    if row+1 < m and target[0] == wordMap[row+1][col]:
        return searchOther(target[1:], row+1, col)

    if row-1 >= 0 and target[0] == wordMap[row-1][col]:
        return searchOther(target[1:], row-1, col)

    if col+1 < n and target[0] == wordMap[row][col+1]:
        return searchOther(target[1:], row, col+1)

    if col - 1 >= 0 and target[0] == wordMap[row][col-1]:
        return searchOther(target[1:], row, col-1)
    return False

def solver(strmap, target):
    for i in range(m):
        for j in range(n):
            if targetWord[0] == strmap[i][j]:
                flag = searchOther(target[1:], i, j)
                if flag:
                    return True
    return False

targetWord = input()
print(solver(wordMap, targetWord))
"""
4 4
abcd
efgh
ijkl
mnop
ok
"""