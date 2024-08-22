first = input('Введите целое число')
second = input('Введите целое число')
third = input('Введите целое число')
if first == second == third:
    print ('3')
elif first == second or first == third or second == third:
    print('2')
else:
    print ('0')