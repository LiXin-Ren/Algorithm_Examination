"""
两个长度为n的序列a，b。问有多少个区间[l,r]满足max(a[l,r])<min(b[l,r])
即a区间的最大值小于b区间的最小值
n<le5
a,b<le9
输入：
第一行一个整数n
第二行n个数，第i个为ai
第三行n个数，第i个为bi
输出：
一行一个整数，表示答案

示例：
3
3 2 1
3 3 3
输出：
3
"""

"""
思路：
1.首先将ab分块，剔除对应位置a>b的，因为这些位置不可能出现在结果中。
2.如果一个小块满足Max(miniA) < min(miniB).说明这个小块任意组合都满足要求，个数为n(n+1)//2
3.如果不满足任意组合，那么选区miniA的最大值，查看那个最大值能出现的最长长度。然后将序列分成了两块。
  最大值左边的一块和最大值右边的一块，相当于把带有最大值的部分都剔除了。然后继续将左右两部分进行”2、3“操作。
"""
# a = [3, 2, 1]
# b = [3, 3, 3]

# a = [1, 2, 5, 4, 3]
# b = [3, 6, 3, 1, 4]

a = [8, 10, 2, 5, 7]
b = [3, 11, 7, 6, 9]

def countSenctence(n):          #计算长度为n的序列能组成多少个子序列
    return n *(n+1) //2

def countList(mini):
    miniA = a[mini[0]: mini[1]]
    miniB = b[mini[0]: mini[1]]
    n = len(miniA)
    if n == 1:
        return 1
    if n == 0:
        return 0
    if max(miniA) < min(miniB):
        return countSenctence(n)

    maxIndex = miniA.index(max(miniA))
    left = maxIndex - 1
    right = maxIndex + 1
    while right < n and miniA[maxIndex] < min(miniB[maxIndex:right+1]):
        right += 1
    while left >= 0 and miniA[maxIndex] < min(miniB[left:maxIndex+1]):
        left -= 1
    containMax = countSenctence(right-left-1) - countSenctence(right-maxIndex-1) - countSenctence(maxIndex - left - 1)
    return containMax + countList([mini[0], left+1 + mini[0]]) + countList([right+mini[0], mini[1]])

def main():
    splits = []
    c = list(map(lambda x:x[0] - x[1], zip(a, b)))
    i = 0
    while i < len(c):
        if c[i] < 0:
            start = i
            i += 1
            while i < len(c) and c[i] < 0:
                i += 1
            splits.append([start, i])
        else:
            i += 1

    num = 0
    for mini in splits:
        num += countList(mini)
    return num

print(main())
#print("jjjj")
