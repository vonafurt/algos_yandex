count = 0


def func1(x, y, p):
    current_unit = x
    units = x
    moved_unit = 0
    hp = y
    enemy = p
    count1 = 0
    while hp > 0 or enemy > 0:
        if hp > 0:
            if hp > current_unit:
                hp -= current_unit
                moved_unit = current_unit
                current_unit = 0
            else:
                current_unit -= hp
                moved_unit += hp
                hp = 0
        if enemy > 0:
            if enemy >= current_unit:
                enemy -= current_unit
                moved_unit += current_unit
                current_unit = 0
            else:
                current_unit -= enemy
                moved_unit += enemy
                enemy = 0
        units -= enemy
        if hp > 0:
            enemy += p
        current_unit = units
        moved_unit = 0
        count1 += 1
        if units <= 0:
            return -1
    return count1

def func(x, y, p):
    a = []
    global count
    if x >= y:
        return 1
    if x > p: #союзников больше чем врагов появляется
        current_unit = x
        moved_unit = 0
        hp = y
        enemy = 0
        count = 0
        while hp > 0:
            if hp <= current_unit:
                res = func1(current_unit, hp, enemy)
                if res > 0:
                    a.append(count + res)
            current_unit -= enemy
            moved_unit += enemy
            enemy = 0
            hp -= current_unit
            moved_unit += current_unit
            current_unit = 0
            enemy += p
            current_unit = moved_unit
            moved_unit = 0
            count += 1
        return min(count, min(a))
    current_unit = x
    units = x
    moved_unit = 0
    hp = y
    enemy = 0
    count = 0
    while hp > 0 or enemy > 0:
        if hp > 0:
            if hp > current_unit:
                hp -= current_unit
                moved_unit = current_unit
                current_unit = 0
            else:
                current_unit -= hp
                moved_unit += hp
                hp = 0
        if enemy > 0:
            if enemy >= current_unit:
                enemy -= current_unit
                moved_unit += current_unit
                current_unit = 0
            else:
                current_unit -= enemy
                moved_unit += enemy
                enemy = 0
        units -= enemy
        if hp > 0:
            enemy += p
        current_unit = units
        moved_unit = 0
        count += 1
        if units <= 0:
            return -1
    return count


x = int(input())
y = int(input())
p = int(input())

#print(game(x, y, p))
print(func(x, y, p))
#print(func1(x, y, p))