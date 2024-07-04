def minAttacks(monsters):
    # 怪物数量
    n = len(monsters)
    # 初始化 dp 数组，dp[i] 表示 i 个怪物的最少攻击次数
    dp = [0] * (n + 1)

    # 遍历每个怪物
    for i in range(1, n + 1):
        # 遍历当前怪物之前的所有怪物
        for j in range(i):
            # 计算当前怪物在生命值减半时对其他怪物造成的伤害次数
            half_damage = monsters[i - 1] // 2
            # 更新 dp[i] 的值，选择当前怪物直接死亡或等待减半后造成伤害的最小攻击次数
            dp[i] = min(dp[i], dp[j] + monsters[i - 1], dp[i - j - 1] + half_damage)

    # 返回所有怪物死亡的最少攻击次数
    return dp[n]


# 示例
# monsters = [3, 2, 4]  # 怪物血量数组
monsters = [1, 6]
print(minAttacks(monsters))  # 输出最少攻击次数
