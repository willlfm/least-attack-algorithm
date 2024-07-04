# import sys
# sys.setrecursionlimit(100000)  # 将递归深度限制设置为1500

def atk_time(monsters, atk_order):
    blood = monsters.copy()
    triggered = [0 for _ in range(len(monsters))]

    for i in range(len(atk_order)):  # monster index starting from 0
        atk_index = atk_order[i]
        if blood[atk_index] == 0:
            return "attacking dead"
        blood, triggered = atk(monsters, blood, atk_index, triggered)
        print(blood)
        if examine_all_death(blood):
            return i + 1
    return "Wrong answer"


def atk(monsters, blood, index, triggered):
    new_triggered = triggered.copy()
    next_blood = blood.copy()
    if blood[index] == 0:
        return next_blood
    next_blood[index] -= 1
    if next_blood[index] <= monsters[index] / 2.0 < blood[index]:  # if attack triggers aoe
        if new_triggered[index] == 0:
            new_triggered[index] = 1
            next_blood, new_triggered = aoe(monsters, next_blood, new_triggered)

    return next_blood, new_triggered


def aoe(monsters, blood, triggered):
    new_triggered = triggered.copy()
    next_blood = blood.copy()
    for i in range(len(blood)):
        if next_blood[i] >= 1:
            next_blood[i] -= 1
        else:
            next_blood[i] = 0

    for i in range(len(blood)):
        if next_blood[i] <= monsters[i] / 2 < blood[i]:
            if new_triggered[i] == 0:
                new_triggered[i] = 1
                next_blood, new_triggered = aoe(monsters, next_blood, new_triggered)

    return next_blood, new_triggered


def examine_all_death(blood):
    for i in range(len(blood)):
        if blood[i] != 0:
            return False
    return True  # denotes no living monsters


def min_through_violence(monsters):
    blood = monsters.copy()
    triggered = [0 for _ in range(len(monsters))]
    order, min_time, triggered = min_atk_recursive(monsters, blood, triggered)

    return order, min_time, triggered


def min_atk_recursive(monsters, blood, triggered):
    new_triggered = triggered.copy()
    if examine_all_death(blood):
        return '', 0, new_triggered

    min_atk = 2 ** 31 - 1  # 对于32位整数来说，这是最大的值
    index = ''
    best_suffix_order = ''

    for i in range(len(monsters)):
        if blood[i] > 0:
            next_blood, psb_triggered = atk(monsters, blood, i, triggered)
            suffix_order, min_atk_psb, psb_triggered = min_atk_recursive(monsters, next_blood, psb_triggered)
            current_atk = 1 + min_atk_psb
            if min_atk > current_atk:
                min_atk = current_atk
                index = str(i)
                best_suffix_order = suffix_order
                new_triggered = psb_triggered
    suffix_order = index + best_suffix_order

    return suffix_order, min_atk, new_triggered


# monsters = [1, 4, 4, 4]
# monsters = [1, 5, 6, 7]
# atk_order = [0, 1, 2, 2, 3, 3, 3]
# triggered = [1, 1, 1, 1, 1]
# print(min_through_violence(monsters))
# print(atk_time(monsters, atk_order))
