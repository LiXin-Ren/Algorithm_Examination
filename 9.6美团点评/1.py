line1 = list(map(int, input().strip().split()))
line2 = list(map(int, input().strip().split()))
N = line1[0]
K = line1[1]

locate0 = []

for i in range(N):
    if line2[i] == 0:
        locate0.append(i)

count0 = len(locate0)
if(K >= count0):
    print(N)

len1 = []
for i in range(count0-K+1):
    locate = []
    inner1 = []
    for j in range(0, i):
        locate.append(locate0[j])
    for j in range(i+K, len(locate0)):
        locate.append(locate0[j])
    inner1.append(locate[0])
    inner1.append(N - locate[-1] - 1)
    for k in range(1, len(locate) - 1):
        inner1.append(locate[k] - locate[k - 1] - 1)
    len1.append(max(inner1))

print(max(len1))