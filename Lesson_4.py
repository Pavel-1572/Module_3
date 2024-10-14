
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(15, 'butick', False)
print_params(115, 'градус')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [15, 'мебель', True]
values_dict = {'a': 1, 'b': 'машина', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [36.6, 'температура']
print_params(*values_list_2, 42)





