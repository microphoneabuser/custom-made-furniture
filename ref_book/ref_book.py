positions = {
    0: "Менеджер",
    1: "Дизайнер",
    2: "Курьер"
}

statuses = {
    0: "Создан",
    1: "В процессе изготовления",
    2: "Изготовлен",
    3: "Доставляется",
    4: "Завершен"
}

def get_ch_positions():
    return '''
Выберите номер должности: 
0 - Менеджер
1 - Дизайнер
2 - Курьер
'''