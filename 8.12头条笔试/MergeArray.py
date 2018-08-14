"""
为了提高文章的质量，每篇文章（假设全是英文）都会有m名编辑进行审核，每个编辑独立工作，会把觉得有问题的句子通过下标记录下来。
比如[1, 10], 1表示病句的第一个字符，10表示并举的最后一个字符，也就是从1到10这101个字符组成的句子，是有问题的。
现在需要把多名编辑有问题的句子合并起来。
A编辑指出是[1, 10],[32, 45]
B:[5, 16], [78, 94]
那么可以合并成[1, 16], [32, 45], [78, 94]

示例：
输入：
3   #3名编辑
1,10;32,45
78,94;5,16
80,100;200,220;16,32
输出：
1,45;78,100;200,220
测试
"""

def main():
    n = int(input())
    editors = []
    for i in range(n):
        indexList = input().split(';')
        for index in indexList:
            editor = list(map(int, index.split(',')))
            editors.append(editor)
    editors.sort(key = lambda x: x[0])

    return MergeArray(editors)

def MergeArray(array):
    res = [array[0]]
    for i in range(1, len(array)):
        if array[i][0] <= res[-1][1]:
            res[-1] = [res[-1][0], max(res[-1][1], array[i][1])]
        else:
            res.append(array[i])
    return res

res = main()
s = ''
for l in res:
    s += str(l[0])+','+str(l[1]) + ';'
print(s.strip(';'))


