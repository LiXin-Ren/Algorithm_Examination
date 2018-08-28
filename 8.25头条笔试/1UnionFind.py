"""
8.25 头条笔试
团队里一共有n个人，每个人提供了自己认识的人的名字，不包括自己。
如果A的名单里有B, 或者B的名单里有A，则代表A与B互相认识，同时如果A认识B，B认识C，那么A与C也会认识。

字节君根据名单将团队氛围m组，每组人数可以不同，但组内的任何一个人都与组内其他所有人直接或间接的认识。
如何确定一个方案，使得团队可以分成m组，并且这个m尽可能小

10
0
5 3 0
8 4 0
9 0
9 0
3 0
0
7 9 0
0
9 7 0

输出：2
"""

"""
加权quick-union
改进：
不是随意将一棵树连接到另一颗树，而是记录每棵数的大小并总是把较小的树连接到较大的树上。
"""
class WeightQuickUnion():
    def __init__(self, N):
        self.count = N
        self.id = [i for i in range(N)]
        self.treeSize = [1 for i in range(N)]

    def findRoot(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        pRoot = self.findRoot(p)
        qRoot = self.findRoot(q)

        if not self.connected(p, q):
            if self.treeSize[p] < self.treeSize[q]:
                self.id[pRoot] = qRoot
                self.treeSize[qRoot] += self.treeSize[pRoot]
            else:
                self.id[qRoot] = pRoot
                self.treeSize[pRoot] += self.treeSize[qRoot]
            self.count -= 1


n = int(input())

wqu = WeightQuickUnion(n)

for i in range(n):
    line = list(map(int, input().split()))
    for num in line:
        if num != 0:
            wqu.union(i, num-1)

print(wqu.count)
#print("id: ", wqu.id)