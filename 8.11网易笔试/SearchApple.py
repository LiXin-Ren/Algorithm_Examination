"""
果园里有N堆苹果，每堆苹果数量为a，小易希望知道从左往右数第X个苹果是属于哪一堆的。
第一行一个数N
第二行n个数ai，表示从左往右数第i堆里有多少个苹果(1<=i<= 1000)
第三行一个数m：表示有m次询问
第四行m个数qi：表示小易想最大第qi个苹果属于哪一堆

test:
input:
4
1 5 2 4
3
3 8 4
"""

def BinarySearch(target, listA):
    index = (len(listA) - 1) // 2
    while True:
        if target <= listA[index]:
            if index - 1 < 0 or target > listA[index - 1]:
                return index
            else:
                index = (index - 1 )// 2
        else:
            if index + 1 > len(listA) or target <= listA[index + 1]:
                return index + 1
            else:
                index = (len(listA) - index - 1) // 2


def main():
    n = int(input())
    apples = list(map(int, input().split()))
    m = int(input())
    quary = list(map(int, input().split()))

    for i in range(1, n):
        apples[i] = apples[i-1] + apples[i]

    res = []
    for i in range(m):
        res.append(BinarySearch(quary[i], apples)+1)
    return res

print(main())