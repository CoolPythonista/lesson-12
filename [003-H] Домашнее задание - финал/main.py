# Создать функцию с параметром ожидающим структуру данных
# с элементами типа число (int) и возвращающую сумму чисел.


def add_nums(values):
    result = 0
    
    for v in values:
        result = result + v
        
    return result


examples = [
    [1, 2, 3],
    [-1, 2, -4, -3],
    [-5, 0, 1, 3, 4, 0],
    [1, -8, 2, 1],
    [0, -6, 5, -6, 7],
    [-4, -1, 10]
]

for ex in examples:
    result = add_nums(ex)
    print(f'{result}   =>   {ex}')


