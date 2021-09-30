from models.order import Order
from models.furniture import Furniture
from models.client import Client
from datetime import datetime
from models.employee import Employee
from models.orders import Orders
from models.furnitures import Furnitures
from models.clients import Clients
from models.employees import Employees
from utils import utils
from ref_book import ref_book
from auth import auth as authorization
from ref_book import help as h
from ref_book.commands import commands_global as cg
from ref_book.commands import commands_clients as cc
from ref_book.commands import commands_employees as ce
from ref_book.commands import commands_furnitures as cf
from ref_book.commands import commands_orders as co
import getpass

employees = Employees()
clients = Clients()
furnitures = Furnitures()
orders = Orders()

user = None

def auth():
    print('Для начала работы войдите в учетную запись.')
    login = input('Введите логин: ')
    password = getpass.getpass('Введите пароль: ')
    global user
    user, message = authorization.authorize(login, password)
    print(message)
    if user:
        read_all()
        help(0)
        main_menu()
    else:
        exit()


def main_menu():
    global user
    command = input(f'\n~{user.login}~: ')
    if command in cg:
        i = cg[command]
        if i == -1:
            exit()
        elif i == 0:
            help(0)
            main_menu()
        elif i == 1:
            clients_menu()
        elif i == 2:
            employees_menu()
        elif i == 3:
            furnitures_menu()
        elif i == 4:
            orders_menu()
    else:
        print('''\nВы ввели что-то непонятное... 
        Прочитайте инструкцию по использованию данной программы:''')
        help(0)
        main_menu()

def clients_menu():
    global user
    command = input(f'\n~{user.login}~/clients: ')
    arr = command.split()
    command = arr[0]
    if command in cc:
        i = cc[command]
        if i == -2:
            main_menu()
        elif i == -1:
            exit()
        elif i == 0:
            help(1)
            clients_menu()
        elif i == 1:
            get_clients()
        elif i == 2:
            try:
                get_client(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(1)
                clients_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                clients_menu()
        elif i == 3:
            add_client()
        elif i == 4:
            try:
                del_client(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(1)
                clients_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                clients_menu()
        elif i == 5:
            try:
                edit_client(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(1)
                clients_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                clients_menu()
    else:
        print('''\nВы ввели что-то непонятное... 
        Прочитайте инструкцию по использованию данной программы:''')
        help(1)
        clients_menu()

def get_clients():
    print()
    print(clients.get_clients_table())
    clients_menu()

def get_client(id: int):
    client = clients.get_by_id(id)
    if client:
        print(client.get_string())
        clients_menu()
    else:
        print('\nНет клиента с заданным ИД.')
        clients_menu()

def add_client():
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите email: ')
    passport = input('Введите паспорт: ')
    date_of_birth = input('Введите дату рождения (через точку - пр: 01.01.2000): ')
    try:
        datetime.strptime(date_of_birth, "%d.%m.%Y")
    except:
        print('Неправильный формат введенных данных!')
        clients_menu()
    global clients
    client = Client(clients.get_new_id(), fio, phone, email, passport, date_of_birth)
    clients.add(client)
    clients.save()
    print('Клиент успешно создан.') 
    clients_menu()

def del_client(id: int):
    ans = input(f'Вы точно хотите удалить клиента №{id}? (y/n)\n')
    if ans == 'y':
        global clients
        ok = clients.delete(id)
        if ok:
            clients.save()
            print('Клиент успешно удален.')
            clients_menu()
        else:
            print('Произошла ошибка при удалении клиента!')
            clients_menu()
    else:
        clients_menu()

def edit_client(id: int):
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите email: ')
    passport = input('Введите паспорт: ')
    date_of_birth = input('Введите дату рождения (через точку - пр: 01.01.2000): ')
    try:
        datetime.strptime(date_of_birth, "%d.%m.%Y")
    except:
        print('Неправильный формат введенных данных!')
        clients_menu()
    client = Client(id, fio, phone, email, passport, date_of_birth)
    global clients
    ok = clients.edit(id, client)
    if ok:
        clients.save()
        print('Клиент успешно изменен.') 
        clients_menu()
    else:
        print('Произошла ошибка при изменении информации о клиенте!')

def employees_menu():
    global user
    command = input(f'\n~{user.login}~/employees: ')
    arr = command.split()
    command = arr[0]
    if command in ce:
        i = ce[command]
        if i == -2:
            main_menu()
        elif i == -1:
            exit()
        elif i == 0:
            help(2)
            employees_menu()
        elif i == 1:
            get_employees()
        elif i == 2:
            try:
                get_employee(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(2)
                employees_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                employees_menu()
        elif i == 3:
            add_employee()
        elif i == 4:
            try:
                del_employee(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(2)
                employees_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                employees_menu()
        elif i == 5:
            try:
                edit_employee(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(2)
                employees_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(2)
                employees_menu()
    else:
        print('''\nВы ввели что-то непонятное... 
        Прочитайте инструкцию по использованию данной программы:''')
        help(2)
        employees_menu()

def get_employees():
    print()
    print(employees.get_employees_table())
    employees_menu()

def get_employee(id: int):
    employee = employees.get_by_id(id)
    if employee:
        print(employee.get_string())
        employees_menu()
    else:
        print('\nНет сотрудника с заданным ИД.')
        employees_menu()

def add_employee():
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите email: ')
    passport = input('Введите паспорт: ')
    position = input(ref_book.get_ch_positions())
    try: 
        position = int(position)
    except ValueError:
        print('Вы ввели данные неправильного формата')
        employees_menu()
    if int(position) not in ref_book.positions.keys():
        print('Нет такой должности.')
        employees_menu()
    login = input('Введите логин: ')
    password = utils.gen_hash(getpass.getpass('Введите пароль: '))
    password_check = utils.gen_hash(getpass.getpass('Введите паспорт еще раз: '))
    if password != password_check:
        print('Неправильный пароль.')
        employees_menu()

    global employees
    employee = Employee(employees.get_new_id(), fio, phone, email, passport, position,
        login, password)
    employees.add(employee)
    employees.save()
    print('Сотрудник успешно создан.')
    employees_menu()

def del_employee(id: int):
    ans = input(f'Вы точно хотите удалить сотрудника №{id}? (y/n)\n')
    if ans == 'y':
        global employees
        ok = employees.delete(id)
        if ok:
            employees.save()
            print('Сотрудник успешно удален.')
            employees_menu()
        else:
            print('Произошла ошибка при удалении сотрудника!')
            employees_menu()
    else:
        employees_menu()

def edit_employee(id: int):
    fio = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    email = input('Введите email: ')
    passport = input('Введите паспорт: ')
    position = input(ref_book.get_ch_positions())
    try: 
        position = int(position)
    except ValueError:
        print('Вы ввели данные неправильного формата')
        employees_menu()
    if position not in ref_book.positions.keys():
        print('Нет такой должности.')
        employees_menu()
    login = input('Введите логин: ')
    password = utils.gen_hash(getpass.getpass('Введите пароль: '))
    password_check = utils.gen_hash(getpass.getpass('Введите паспорт еще раз: '))
    if password != password_check:
        print('Неправильный пароль.')
        employees_menu()
    
    global clients
    employee = Employee(id, fio, phone, email, passport, position,
        login, password)
    ok = employees.edit(id, employee)
    if ok:
        employees.save()
        print('Сотрудник успешно изменен.') 
        employees_menu()
    else:
        print('Произошла ошибка при изменении информации о сотруднике!')


def furnitures_menu():
    global user
    command = input(f'\n~{user.login}~/furnitures: ')
    arr = command.split()
    command = arr[0]
    if command in cf:
        i = cf[command]
        if i == -2:
            main_menu()
        elif i == -1:
            exit()
        elif i == 0:
            help(3)
            furnitures_menu()
        elif i == 1:
            get_furnitures()
        elif i == 2:
            try:
                get_furniture(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(3)
                furnitures_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(3)
                furnitures_menu()
        elif i == 3:
            add_furniture()
        elif i == 4:
            try:
                del_furniture(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(3)
                furnitures_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(3)
                furnitures_menu()
        elif i == 5:
            try:
                edit_furniture(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(3)
                furnitures_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(3)
                furnitures_menu()
    else:
        print('''\nВы ввели что-то непонятное... 
        Прочитайте инструкцию по использованию данной программы:''')
        help(3)
        furnitures_menu()

def get_furnitures():
    print()
    print(furnitures.get_furnitures_table())
    furnitures_menu()

def get_furniture(id: int):
    furniture = furnitures.get_by_id(id)
    if furniture:
        print(furniture.get_string())
        furnitures_menu()
    else:
        print('\nНет мебели с заданным ИД.')
        furnitures_menu()


def add_furniture():
    try: 
        kind = input('Введите вид мебели: ')
        height = input('Введите высоту: ')
        width = input('Введите ширину: ')
        length = input('Введите длину: ')
        n_materials = input('Введите количество материалов: ')
        n_materials = int(n_materials)
        materials = []
        for i in range(n_materials):
            materials.append({'name':input('Введите материал №' + str(i + 1) + ': ')})
        color = input('Введите цвет: ')
        price = float(input('Введите цену: ') )
    except ValueError:
        print('Вы ввели данные неправильного формата')
        furnitures_menu()

    global furnitures
    furniture = Furniture(furnitures.get_new_id(), kind, height, width, length, 
        materials, color, price)  
    furnitures.add(furniture)
    furnitures.save()
    print('Мебель успешно создана.')
    furnitures_menu()

def del_furniture(id: int):
    ans = input(f'Вы точно хотите удалить мебель №{id}? (y/n)\n')
    if ans == 'y':
        global furnitures
        ok = furnitures.delete(id)
        if ok:
            furnitures.save()
            print('Мебель успешно удалена.')
            furnitures_menu()
        else:
            print('Произошла ошибка при удалении мебели!')
            furnitures_menu()
    else:
        furnitures_menu()

def edit_furniture(id: int):
    try: 
        kind = input('Введите вид мебели: ')
        height = input('Введите высоту: ')
        width = input('Введите ширину: ')
        length = input('Введите длину: ')
        n_materials = input('Введите количество материалов: ')
        n_materials = int(n_materials)
        materials = []
        for i in range(n_materials):
            materials.append({'name':input('Введите материал №' + str(i + 1) + ': ')})
        color = input('Введите цвет: ')
        price = float(input('Введите цену: ') )
    except ValueError:
        print('Вы ввели данные неправильного формата')
        furnitures_menu()
    
    global furnitures
    furniture = Furniture(furnitures.get_new_id(), kind, height, width, length, 
        materials, color, price)
    ok = furnitures.edit(id, furniture)
    if ok:
        furnitures.save()
        print('Мебель успешно изменена.') 
        furnitures_menu()
    else:
        print('Произошла ошибка при изменении информации о мебели!')



def orders_menu():
    global user
    command = input(f'\n~{user.login}~/orders: ')
    arr = command.split()
    command = arr[0]
    if command in co:
        i = co[command]
        if i == -2:
            main_menu()
        elif i == -1:
            exit()
        elif i == 0:
            help(4)
            orders_menu()
        elif i == 1:
            get_orders()
        elif i == 2:
            try:
                get_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 3:
            add_order()
        elif i == 4:
            try:
                fur_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 5:
            try:
                designer_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 6:
            try:
                manager_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 7:
            try:
                courier_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 8:
            try:
                set_pre_pay(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 9:
            try:
                set_made(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 10:
            try:
                set_delivery(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 11:
            try:
                set_done(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 12:
            try:
                del_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 13:
            try:
                edit_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
        elif i == 14:
            try:
                del_fur_order(int(arr[1]))
            except IndexError:
                print('Вы забыли ввести ИД...')
                help(4)
                orders_menu()
            except ValueError:
                print('Вы ввели что-то странное...')
                help(4)
                orders_menu()
    else:
        print('''\nВы ввели что-то непонятное... 
        Прочитайте инструкцию по использованию данной программы:''')
        help(4)
        orders_menu()

def get_orders():
    print()
    global furnitures, clients, employees
    print(orders.get_orders_table(furnitures, clients, employees))
    orders_menu()

def get_order(id: int):
    order = orders.get_by_id(id)
    if order:
        global furnitures, clients, employees
        print(order.get_string(furnitures, clients, employees))
        orders_menu()
    else:
        print('\nНет заказов с заданным ИД.')
        orders_menu()

def add_order():
    try: 
        global furnitures, clients, employees

        n_furs = input('Введите количество мебели: ')
        n_furs = int(n_furs)
        furniture_ids = []
        print(furnitures.get_furnitures_table())
        for i in range(n_furs):
            furniture_ids.append(int(input('Введите ИД мебели №' + str(i + 1) + ' в данном заказе: ')))
        print(clients.get_clients_table())
        client_id = int(input('Введите ИД клиента: '))
        print(employees.get_emps_by_position_table(1))
        designer_id = int(input('Введите ИД дизайнера (при отсутствии введите \"0\"): '))
        if not employees.is_designer(designer_id):
            print('\nВыбранный вами сотрудник не является дизайнером.')
            orders_menu()
        if designer_id == 0:
            designer_id = None 
        print(employees.get_emps_by_position_table(0))
        manager_id = int(input('Введите ИД менеджера (при отсутствии введите \"0\"): '))
        if not employees.is_manager(manager_id):
            print('\nВыбранный вами сотрудник не является менеджером.')
            orders_menu()
        if manager_id == 0:
            manager_id = None
        print(employees.get_emps_by_position_table(2))
        courier_id = int(input('Введите ИД курьера (при отсутствии введите \"0\"): '))
        if not employees.is_courier(courier_id):
            print('\nВыбранный вами сотрудник не является курьером.')
            orders_menu()
        if courier_id == 0:
            courier_id = None
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()

    global orders
    order = Order(orders.get_new_id(), client_id, designer_id=designer_id, manager_id=manager_id,
        courier_id=courier_id)  
    order.add_furnitures_from_list(furniture_ids)
    order.count_cost(furnitures)
    orders.add(order)
    orders.save()
    print('\nЗаказ успешно создан.')
    orders_menu()

def fur_order(id: int):
    global furnitures, orders
    print(furnitures.get_furnitures_table())
    try:
        fur_id = int(input('Введите ИД мебели, которую хотите добавить в заказ №' + str(id) + ': '))
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    if furnitures.get_by_id(fur_id) == None:
        print('\nНет мебели с таким ИД.')
        orders_menu()
    order = orders.get_by_id(id)
    order.add_furniture(fur_id)
    order.count_cost(furnitures)
    orders.edit(id, order)
    orders.save()
    print('\nМебель успешно добавлена к заказу.')
    orders_menu()

def del_fur_order(id: int):
    global furnitures, orders
    try:
        fur_id = int(input('Введите ИД мебели, которую хотите удалить из заказа №' + str(id) + ': '))
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    order = orders.get_by_id(id)
    for i in order.furniture_ids:
        if i == {'id': fur_id}:
            order.del_furniture(fur_id)
            order.count_cost(furnitures)
            orders.edit(id, order)
            orders.save()
            print('\nМебель успешно удалена из заказа.')
            orders_menu()
            
    print('\nНет мебели с таким ИД.')
    orders_menu()
            

def designer_order(id: int):
    global orders, employees
    print(employees.get_emps_by_position_table(1))
    try:
        designer_id = int(input('Введите ИД дизайнера, которого хотите назначить на заказ №' + str(id) + ': '))
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    des = employees.get_by_id(designer_id)
    if des == None:
        print('\nНет сотрудника с таким ИД.')
        orders_menu()
    if des.position != 1:
        print('\nСотрудник ' + des.fio + ' не является дизайнером.')
        orders_menu()
    order = orders.get_by_id(id)
    order.set_designer(designer_id)
    orders.edit(id, order)
    orders.save()
    print('\nДизайнер успешно назначен на заказ.')
    orders_menu()

def manager_order(id: int):
    global orders, employees
    print(employees.get_emps_by_position_table(0))
    try:
        manager_id = int(input('Введите ИД менеджера, которого хотите назначить на заказ №' + str(id) + ': '))
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    manager = employees.get_by_id(manager_id)
    if manager == None:
        print('\nНет сотрудника с таким ИД.')
        orders_menu()
    if manager.position != 0:
        print('\nСотрудник ' + manager.fio + ' не является менеджером.')
        orders_menu()
    order = orders.get_by_id(id)
    order.set_manager(manager_id)
    orders.edit(id, order)
    orders.save()
    print('\nМенеджер успешно назначен на заказ.')
    orders_menu()

def courier_order(id: int):
    global orders, employees
    print(employees.get_emps_by_position_table(2))
    try:
        courier_id = int(input('Введите ИД курьера, которого хотите назначить на заказ №' + str(id) + ': '))
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    courier = employees.get_by_id(courier_id)
    if courier == None:
        print('\nНет сотрудника с таким ИД.')
        orders_menu()
    if courier.position != 2:
        print('\nСотрудник ' + courier.fio + ' не является курьером.')
        orders_menu()
    order = orders.get_by_id(id)
    order.set_courier(courier_id)
    orders.edit(id, order)
    orders.save()
    print('\nКурьер успешно назначен на заказ.')
    orders_menu()

def set_pre_pay(id: int):
    global orders
    order = orders.get_by_id(id)
    if order == None:
        print('\nНет заказа с таким ИД.')
        orders_menu()
    try:
        order.pre_pay = float(input('Введите сумму предоплаты: '))
        order.status = 1
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()
    orders.edit(id, order)
    orders.save()
    print('\nПредоплата успешно внесена.')
    orders_menu()

def set_made(id: int):
    global orders
    order = orders.get_by_id(id)
    if order == None:
        print('\nНет заказа с таким ИД.')
        orders_menu()
    if input('\nВы точно хотите присвоить заказу статус \"Изготовлен\"? (y/n)\n') == 'y':
        order.status = 2
        orders.edit(id, order)
        orders.save()
        print('\nЗаказ изготовлен.')
    orders_menu()

def set_delivery(id: int):
    global orders, employees
    order = orders.get_by_id(id)
    if order == None:
        print('\nНет заказа с таким ИД.')
        orders_menu()
    if input('\nВы точно хотите перенести заказ в стадию доставки? (y/n)\n') == 'y':
        if order.courier_id == None:
            print(employees.get_emps_by_position_table(2))
            try:
                courier_id = int(input('Введите ИД курьера, которого хотите назначить на заказ №' + str(id) + ': '))
            except ValueError:
                print('\nВы ввели данные неправильного формата')
                orders_menu()
            courier = employees.get_by_id(courier_id)
            if courier == None:
                print('\nНет сотрудника с таким ИД.')
                orders_menu()
            if courier.position != 2:
                print('\nСотрудник ' + courier.fio + ' не является курьером.')
                orders_menu()
            order.set_courier(courier_id)
        order.status = 3
        orders.edit(id, order)
        orders.save()
        print('\nЗаказ успешно перенесен в стадию доставки.')
    orders_menu()

def set_done(id: int):
    global orders
    order = orders.get_by_id(id)
    if order == None:
        print('\nНет заказа с таким ИД.')
        orders_menu()
    if input('\nВы точно хотите завершить заказ? (y/n)\n') == 'y':
        order.status = 4
        orders.edit(id, order)
        orders.save()
        print('\nЗаказ успешно завершен.')
    orders_menu()

def del_order(id: int):
    ans = input(f'Вы точно хотите удалить заказ №{id}? (y/n)\n')
    if ans == 'y':
        global orders
        ok = orders.delete(id)
        if ok:
            orders.save()
            print('\nЗаказ успешно удален.')
            orders_menu()
        else:
            print('\nПроизошла ошибка при удалении заказа!')
            orders_menu()
    else:
        orders_menu()

def edit_order(id: int):
    try: 
        global furnitures, clients, employees

        n_furs = input('Введите количество мебели: ')
        n_furs = int(n_furs)
        furniture_ids = []
        print(furnitures.get_furnitures_table())
        for i in range(n_furs):
            furniture_ids.append(int(input('Введите ИД мебели №' + str(i + 1) + ' в данном заказе: ')))
        print(clients.get_clients_table())
        client_id = int(input('Введите ИД клиента: '))
        print(employees.get_emps_by_position_table(1))
        designer_id = int(input('Введите ИД дизайнера (при отсутствии введите \"0\"): '))
        if not employees.is_designer(designer_id):
            print('\nВыбранный вами сотрудник не является дизайнером.')
            orders_menu()
        if designer_id == 0:
            designer_id = None 
        print(employees.get_emps_by_position_table(0))
        manager_id = int(input('Введите ИД менеджера (при отсутствии введите \"0\"): '))
        if not employees.is_manager(manager_id):
            print('\nВыбранный вами сотрудник не является менеджером.')
            orders_menu()
        if manager_id == 0:
            manager_id = None
        print(employees.get_emps_by_position_table(2))
        courier_id = int(input('Введите ИД курьера (при отсутствии введите \"0\"): '))
        if not employees.is_courier(courier_id):
            print('\nВыбранный вами сотрудник не является курьером.')
            orders_menu()
        if courier_id == 0:
            courier_id = None
    except ValueError:
        print('\nВы ввели данные неправильного формата')
        orders_menu()

    global orders
    order = Order(orders.get_new_id(), client_id, designer_id=designer_id, manager_id=manager_id,
        courier_id=courier_id)  
    order.add_furnitures_from_list(furniture_ids)
    order.count_cost(furnitures)
    ok = orders.edit(id, order)
    if ok:
        orders.save()
        print('\nЗаказ успешно изменен.') 
        orders_menu()
    else:
        print('\nПроизошла ошибка при изменении информации о заказе!')



def help(i):
    if i == 0:
        print(h.help_global)
    elif i == 1:
        print(h.help_clients)
    elif i == 2:
        print(h.help_employees)
    elif i == 3:
        print(h.help_furnitures)
    elif i == 4:
        print(h.help_orders)

def read_all():
    global employees
    global clients
    global furnitures
    global orders
    employees.read()
    clients.read()
    furnitures.read()
    orders.read()

print('\n/           /                Приветствую вас!                     \           \ \n')

auth()