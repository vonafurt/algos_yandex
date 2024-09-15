import re


def func(data):
    global matches, count, last_time, first_score, second_score

    if data[0].startswith('"'):
        parts = data.split(" - ")
        team1 = parts[0].strip('"')
        team2_and_scores = parts[1].split()
        team2 = team2_and_scores[:-1]
        team2_string = ' '.join(team2_and_scores[0:-1]).strip('"')
        scores = team2_and_scores[-1].split(':')
        matches.append({team1: int(scores[0]), team2_string: int(scores[1])})
        first_score = int(scores[0])
        second_score = int(scores[1])
        last_time = -1
        count += 1
        matches[count]['players1'] = {}
        matches[count]['players2'] = {}
        return 0

    elif data[-1].endswith("'"):  # добавление игрока
        parts = data.split()
        name = ' '.join(parts[:-1])
        minutes = int(parts[-1].strip("'"))
        if first_score > 0:
            if name in matches[count]['players1']:
                matches[count]['players1'][name].append(minutes)
            else:
                matches[count]['players1'][name] = [minutes]
            first_score -= 1
        else:
            if name in matches[count]['players2']:
                matches[count]['players2'][name].append(minutes)
            else:
                matches[count]['players2'][name] = [minutes]

    elif data.startswith('Total goals for'):  # количество голов забитое командой за все матчи
        cnt = 0
        data = re.findall(r'[\w]+|"[^"]+"', data)
        data[-1] = data[-1][1:-1]
        for i in range(count + 1):
            if data[-1] in matches[i]:
                cnt += matches[i][data[-1]]
        print(cnt)

    elif data.startswith('Total goals by'):  # количество голов забитое игроком за все матчи
        cnt = 0
        data = data.split(' ', 3)
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                cnt += len(matches[i]['players1'][data[-1]])
            if data[-1] in matches[i]['players2']:
                cnt += len(matches[i]['players2'][data[-1]])
        print(cnt)

    elif data.startswith('Mean goals per game for'):  # среднее количество голов забиваемое командой за 1 матч
        cnt = 0
        games = 0
        data = re.findall(r'[\w]+|"[^"]+"', data)
        data[-1] = data[-1][1:-1]
        for i in range(count + 1):
            if data[-1] in matches[i]:
                cnt += matches[i][data[-1]]
                games += 1
        print(cnt / games)

    elif data.startswith('Mean goals per game by'):  # среднее количество голов забиваемое игроком за 1 матч
        data = data.split(' ', 5)
        cnt = 0
        team = ''
        games = 0
        flag = 0
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                cnt += len(matches[i]['players1'][data[-1]])
                if flag == 0:
                    team = list(matches[i].keys())[0]
                    flag = 1
            if data[-1] in matches[i]['players2']:
                cnt += len(matches[i]['players2'][data[-1]])
                if flag == 0:
                    team = list(matches[i].keys())[1]
                    flag = 1
        if team != '':
            for i in range(count + 1):
                if team in matches[i]:
                    games += 1
            print(cnt / games)
        else:
            print(0)

    elif data.startswith('Goals on minute'):  # кол-во голов забитое игроком на конкретной минуте
        cnt = 0
        data = data.split(' ', 5)
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                if int(data[3]) in matches[i]['players1'][data[-1]]:
                    cnt += 1
            if data[-1] in matches[i]['players2']:
                if int(data[3]) in matches[i]['players2'][data[-1]]:
                    cnt += 1
        print(cnt)

    elif data.startswith('Goals on first'):  # кол-во голов забитое игроком до какой то минуты
        data = data.split(' ', 6)
        cnt = 0
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                for num in matches[i]['players1'][data[-1]]:
                    if num <= int(data[3]):
                        cnt += 1
            if data[-1] in matches[i]['players2']:
                for num in matches[i]['players2'][data[-1]]:
                    if num <= int(data[3]):
                        cnt += 1
        print(cnt)

    elif data.startswith('Goals on last'):  # кол-во голов забитое игроком после какой то минуты
        data = data.split(' ', 6)
        cnt = 0
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                for num in matches[i]['players1'][data[-1]]:
                    if num >= 91 - int(data[3]):
                        cnt += 1
            if data[-1] in matches[i]['players2']:
                for num in matches[i]['players2'][data[-1]]:
                    if num >= 91 - int(data[3]):
                        cnt += 1
        print(cnt)

    elif data.startswith('Score opens by "'):  # сколько раз данная команда открывала счет в матче
        cnt = 0
        min1 = 100
        min2 = 100
        data = re.findall(r'[\w]+|"[^"]+"', data)
        data[-1] = data[-1][1:-1]
        for i in range(count + 1):
            if data[-1] == list(matches[i].keys())[0]:
                for keys, values in matches[i]['players1'].items():
                    if int(min1) > int(min(values)):
                        min1 = int(min(values))
                for keys, values in matches[i]['players2'].items():
                    if int(min2) > int(min(values)):
                        min2 = int(min(values))
                if min1 < min2:
                    cnt += 1
            if data[-1] == list(matches[i].keys())[1]:
                for keys, values in matches[i]['players1'].items():
                    if int(min1) > int(min(values)):
                        min1 = int(min(values))
                for keys, values in matches[i]['players2'].items():
                    if int(min2) > int(min(values)):
                        min2 = int(min(values))
                if min1 > min2:
                    cnt += 1
            min1 = 100
            min2 = 100
        print(cnt)

    elif data.startswith('Score opens by'):  # сколько раз игрок открывал счет в матче
        data = data.split(' ', 3)
        cnt = 0
        min1 = 100
        min2 = 100
        for i in range(count + 1):
            if data[-1] in matches[i]['players1']:
                min1 = int(min(matches[i]['players1'][data[-1]]))
                for keys, values in matches[i]['players1'].items():
                    if keys != data[-1]:
                        if int(min2) > int(min(values)):
                            min2 = int(min(values))
                for keys, values in matches[i]['players2'].items():
                    if int(min2) > int(min(values)):
                        min2 = int(min(values))
            if data[-1] in matches[i]['players2']:
                min1 = min(matches[i]['players2'][data[-1]])
                for keys, values in matches[i]['players2'].items():
                    if keys != data[-1]:
                        if int(min2) > int(min(values)):
                            min2 = int(min(values))
                for keys, values in matches[i]['players1'].items():
                    if int(min2) > int(min(values)):
                        min2 = int(min(values))
            if min1 < min2:
                cnt += 1
            min1 = 100
            min2 = 100
        print(cnt)


last_time = -1
matches = []
count = -1
first_score = 0
second_score = 0

with open("input.txt", "r") as file:
    # Читаем все строки из файла и удаляем лишние пробельные символы
    data = [line.strip() for line in file.readlines()]

for item in data:
    func(item)
    print(matches)
    # print(matches)
    # print(matches)
