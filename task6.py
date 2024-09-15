n = input()
numbers = input().split()
mas = [1 if int(num) % 2 == 0 else 0 for num in numbers]

current_index = 0
next_index = 1

while next_index < len(mas):
    if mas[current_index] == mas[next_index]:
        if mas[current_index] == 0:
            print('x', end="")
        else:
            print('+', end="")
        mas[current_index] = mas[next_index]
        next_index += 1
    else:
        print('+', end="")
        mas[current_index] = 0
        next_index += 1