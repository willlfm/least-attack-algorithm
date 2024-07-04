# import sys
# sys.setrecursionlimit(100000)  # 将递归深度限制设置为1500


def atk_time(monsters, atk_order):
    blood = monsters.copy()

    for i in range(len(atk_order)):  # monster index starting from 0
        atk_index = atk_order[i]
        if blood[atk_index] == 0:
            return "attacking dead"
        blood = atk(monsters, blood, atk_index)
        if examine_all_death(blood):
            return i + 1
    return "Wrong answer"


def atk(monsters, blood, index):
    next_blood = blood.copy()
    if blood[index] == 0:
        return next_blood
    next_blood[index] -= 1
    if next_blood[index] <= monsters[index] / 2.0 < blood[index]:  # if attack triggers aoe
        next_blood = aoe(monsters, next_blood)

    return next_blood


def aoe(monsters, blood):
    next_blood = blood.copy()
    for i in range(len(blood)):
        if next_blood[i] >= 1:
            next_blood[i] -= 1
        else:
            next_blood[i] = 0

    for i in range(len(blood)):
        if next_blood[i] <= monsters[i] / 2 < blood[i]:
            next_blood = aoe(monsters, next_blood)

    return next_blood


def examine_all_death(blood):
    for i in range(len(blood)):
        if blood[i] != 0:
            return False
    return True  # denotes no living monsters


def min_through_violence(monsters):
    blood = monsters.copy()
    order, min_time = min_atk_recursive(monsters, blood)

    return order, min_time


def min_atk_recursive(monsters, blood):
    if examine_all_death(blood):
        return '', 0

    min_atk = 2 ** 31 - 1  # 对于32位整数来说，这是最大的值
    index = ''
    best_suffix_order = ''

    for i in range(len(monsters)):
        if blood[i] > 0:
            next_blood = atk(monsters, blood, i)
            suffix_order, min_atk_psb = min_atk_recursive(monsters, next_blood)
            current_atk = 1 + min_atk_psb
            if min_atk > current_atk:
                min_atk = current_atk
                index = str(i)
                best_suffix_order = suffix_order
    suffix_order = index + best_suffix_order

    return suffix_order, min_atk


# monsters = [1, 1, 1, 1, 6]
monsters = [1, 5, 6, 7]
atk_order = [1, 1, 2, 0, 3]
# print(atk_time(monsters, atk_order))
print(min_through_violence(monsters))
print(atk_time(monsters, atk_order))
