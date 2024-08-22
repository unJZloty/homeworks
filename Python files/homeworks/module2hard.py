pass_ = []
num = int(input('Введите число от 3 до 20:'))
for i in range(1, 21):
    for j in range(1, 21):
        if i != j and i < j and num % (i + j) == 0:
            pass_.append(i)
            pass_.append(j)
print(''.join(map(str, pass_)))