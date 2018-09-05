import math
p = list(map(int, input().split()))
q = list(map(int, input().split()))
KL = 0.0
pPro = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
qPro = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for x in p:
    pPro[x] += 1

for y in q:
    qPro[y] += 1


for i in range(1, 7):
    if qPro[i] != 0:
        KL += (pPro[i]/len(p)) * math.log((pPro[i]/len(p)) / (qPro[i])/len(q), 2)
print(round(KL, 2))
