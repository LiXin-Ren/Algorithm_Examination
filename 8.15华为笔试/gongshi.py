def main():
    s = input()
    l = []
    i = 0
    while i < len(s):
        num = 0
        if s[i] == '(' or s[i] == '+' or s[i] == '*':
            l.append(s[i])
            i += 1
        if s[i] == ' ':
            continue
        while i < len(s) and s[i] >= '0' and s[i] <='9':
            num *= 10
            num += int(s[i])
            i += 1
        if s[i] == ')':
            if len(l) >= 3:
                tmp1 = l.pop()
                if type(tmp1) != int:
                    return -1
                tmp2 = l.pop()
                if tmp2 == '^':
                    l.append(tmp1 + 1)
                    break
                if type(tmp2) != int:
                    return -1
                tmp3 = l.pop()
                if tmp3 == '+':
                    l.append(tmp1 + tmp2)
                if tmp3 == '*':
                    l.append(tmp1 * tmp2)
                else:
                    return -1





