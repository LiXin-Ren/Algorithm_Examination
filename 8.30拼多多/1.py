import math
hp = int(input())
normalA = int(input())
bufferA = int(input())

if normalA*2 >= bufferA:
    print(math.ceil(hp/normalA))

else:
    resHp = hp
    num = 0

    num = (hp // bufferA)       #聚力次数
    resHp = hp - num*bufferA

    num *= 2
    while resHp > 0:
        resHp -= normalA
        num += 1
    print(num)



