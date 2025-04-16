# Чат-бот для записи гостей в кафе.

def order(open_tables, busy_tables):
    print("Добро пожаловать в кафе: ***'* Звезда Мишлен!")
    
    while True:
        print('-' * 45)
        print('Пожалуйста выберите час для заказа столика:')
        
        for open_table in open_tables:
            
            if open_table in busy_tables:
                continue
            else:
                print('-' * 5, open_table)
        
        order = input('\nВведите час (11/12/13 и т.д.): ')
        order_format  = f'{order}:00'
        
        if order_format in open_tables:
            busy_tables.append(order_format)
        else:
            print('-' * 5, 'Неверно выбрано время!\n')

        if open_tables == busy_tables:
            print('\nК сожалению свободных столиков больше нет.')
            break


open_tables = ['14:00', '15:00', '16:00']
busy_tables = []

order(open_tables, busy_tables)














