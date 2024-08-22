def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(a=2, b = 3)
print_params(b = 'Thrue')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [7, 'Bullet', True]
values_dict = {'a': False, 'b': 777, 'c': 'Gun'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3.14, False]
print_params(*values_list_2, 42)