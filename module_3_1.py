from statistics import linear_regression

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple_ = (len(string), string.upper(), string.lower())
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    f = False
    while len(list_to_search) > 0:
        a = list_to_search[0].lower()
        if a == string.lower():
            f = True
        list_to_search.pop(0)
    return f

print(string_info('Шкаф'))
print(string_info('Малыш'))
print(string_info('Пингвин'))
print(is_contains('Dimas', ['DimAS', 'palas', 'Karkas']))
print(is_contains('aaaaa', ['aAAa', 'Ilar', 'GilLLA']))
print(is_contains('anTon', ['sal', 'sel', 'Kirill']))
print(is_contains('pen', ['Door', 'Bool', 'PEN']))
print(calls)