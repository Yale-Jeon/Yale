from itertools import combinations


def is_in(menu, order):
    for m in menu:
        if m not in order:
            return False
    return True


def solution(orders, course):
    result = []
    n_table = []
    answer = []
    d = {}
    for order in orders:
        n_table.append(len(order))

    for i in course:
        max_cnt = 0
        max_menu = []
        lst = []
        for j in range(len(orders)):
            if n_table[j] >= i:
                lst.append(orders[j])
        for k in range(len(lst) - 1):
            menus = list(combinations(lst[k], i))
            for menu in menus:
                if menu in d:
                    continue
                cnt = 1
                for l in range(len(lst) - k - 1):
                    if is_in(menu, lst[k + l + 1]):
                        cnt += 1
                if cnt > 1:
                    d[menu] = cnt
                    if cnt > max_cnt:
                        max_cnt = cnt
                        max_menu = [menu]
                    elif cnt == max_cnt:
                        max_menu.append(menu)
        result += max_menu

    for s in result:
        z = list(s)
        z.sort()
        x = ''
        for ss in z:
            x += ss
        answer.append(x)
    answer.sort()

    return answer