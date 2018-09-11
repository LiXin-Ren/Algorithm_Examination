"""
一串数字能写成多少个不同的ip地址
"""

def Solver(length, s, result):
    if not s:
        if length == 4:
            result.append(1)
        return
    if length == 4:
        return

    Solver(length + 1, s[1:], result)

    if s[0] != '0':
        if len(s) >= 2:
            Solver(length + 1, s[2:], result)
        if len(s) >= 3 and int(s[:3]) <= 255:
            Solver(length + 1, s[3:], result)
    return len(result)


aStr = input()
print(Solver(0, aStr, []))
