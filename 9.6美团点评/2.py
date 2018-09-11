
nk = list(map(int, input().split()))
n = nk[0]
k = nk[1]

values = list(map(int, input().split()))
#maxNum = 0
res = []
for i in range(n-k-1):
    j = i + 1
    #if values[i]
    while j <= n and sum(values[i:j]) + k > j-i:
        j += 1
    res.append(j-i+1)
print(max(res))
#    print(max(res))
    #return max(res)
#     if n <= k:
#         print(n)
#     else:
#         values = list(map(int, input().split()))
#         maxNum = 0
#         for i in range(n - k - 1):
#             j = i + 1
#         while (j < n) and (sum(values[i:j]) + k) > j - i:
#             j += 1
#         if maxNum < j - i + 1:
#             maxNum = j - i + 16
        #return maxNum

