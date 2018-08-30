"""
聚力还是攻击
13
3
5

5
"""
import math
hp = int(input())
normalA = int(input())
bufferA = int(input())

if normalA*2 >= bufferA:    # 两次普通攻击的伤害大于辅助技能的伤害，那么就不用辅助技能。
    print(math.ceil(hp/normalA))

else:
    num = (hp // bufferA)       #聚力次数
    resHp = hp - num*bufferA


    if math.ceil(resHp/normalA) >= 2:
        print((num+1)*2)
    else:
        print(num*2+math.ceil(resHp/normalA))




