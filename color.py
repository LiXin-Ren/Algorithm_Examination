"""
着色问题
有M种颜色，给一个大小为N的扇形着色，要求相邻区域的颜色不能相同，问有几种方式
对于这里用N来做递归的原因 
N,M 考虑两种情况，新加的第N块扇形的颜色跟旁边两块相关，

1.  如果旁边两块颜色不同 那么是color(N-1,M)，那么第N块有M-2种颜色，有color(N-1,M)*（M-2）种可能；

2.  如果旁边两块颜色相同 那么是color(N-2,M)（相当于可以随便去掉第N块旁边的一块不影响讨论），那么第N块有M-1种颜色，有color(N-2,M)*（M-1）种可能；


"""
def color(N, M):
    if N == 1:
        return M
    elif N == 2:
        return (M-1)*M
    elif N == 3:
        return (M-2)*(M-1)*M
    else:
        return color((N - 1), M)*(M-2) + color((N-2), M)*(M-1)
print(color(4, 4))

