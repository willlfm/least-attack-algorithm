import attackTime


def minAttacks(monsters):
    monsters.sort()
    print(monsters)
    triggered = [0 for _ in range(len(monsters))]
    time = 0
    for i in range(len(monsters)):
        if monsters[i] > 0:
            time += 1
            monsters, triggered = attackTime.atk(monsters, monsters, i, triggered)
            print(monsters)
    return time


monsters = [1, 1, 1, 1, 5]  # 怪物血量数组
print(minAttacks(monsters))  # 输出最少攻击次数
