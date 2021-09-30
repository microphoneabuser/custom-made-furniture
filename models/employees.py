import json
from models.employee import Employee
import utils.utils as utils
import os, json
import pandas as pd

class Employees:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'repo/employees.json')

    def __init__(self):
        self.__employees = list()

    def __len__(self):
        return len(self.__employees)

    def __iter__(self):
        return EmployeesIterator(self.__employees)

    def add(self, employee: Employee):
        self.__employees.append(employee)
        return employee.id
    
    def delete(self, id: int):
        emp = self.get_by_id(id)
        if emp:
            self.__employees.remove(emp)
            return True
        return False
    
    def edit(self, id: int, employee: Employee):
        emp = self.get_by_id(id)
        if emp:
            emp.fio = employee.fio
            emp.phone = employee.phone
            emp.email = employee.email
            emp.passport = employee.passport
            emp.position = employee.position
            emp.login = employee.login
            emp.password_hash = employee.password_hash
            return True
        return False

    def get_by_id(self, id: int):
        for emp in self.__employees:
            if emp.id == id:
                return emp
        return None
    
    def save(self):
        utils.save(self.__filename, self.__employees)

    def read(self):
        self.__employees = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            employee = Employee(elem['id'], elem['fio'], elem['phone'], elem['email'], 
                elem['passport'], elem['position'], elem['login'], elem['password_hash'])
            self.add(employee)

    def get_employees_table(self):
        id_arr = []
        fio_arr = []
        phone_arr = []
        email_arr = []
        passport_arr = []
        position_arr = []
        login_arr = []
        password_hash_arr = []
        for elem in self.__employees:
            id_arr.append(elem.id)
            fio_arr.append(elem.fio)
            phone_arr.append(elem.phone)
            email_arr.append(elem.email)
            passport_arr.append(elem.passport)
            position_arr.append(elem.get_position())
            login_arr.append(elem.login)
            password_hash_arr.append(elem.password_hash[:8] + '...')
        return pd.DataFrame(
            {"ИД": id_arr,
            "ФИО": fio_arr,
            "Номер телефона": phone_arr,
            "Email": email_arr,
            "Паспорт": passport_arr,
            "Должность": position_arr,
            "Логин": login_arr,
            "Хеш пароля": password_hash_arr,},
            index=None)

    def get_emps_by_position_table(self, position: int):
        id_arr = []
        fio_arr = []
        phone_arr = []
        email_arr = []
        passport_arr = []
        position_arr = []
        login_arr = []
        for elem in self.__employees:
            if elem.position == position:
                id_arr.append(elem.id)
                fio_arr.append(elem.fio)
                phone_arr.append(elem.phone)
                email_arr.append(elem.email)
                passport_arr.append(elem.passport)
                position_arr.append(elem.get_position())
                login_arr.append(elem.login)
        return pd.DataFrame(
            {"ИД": id_arr,
            "ФИО": fio_arr,
            "Номер телефона": phone_arr,
            "Email": email_arr,
            "Паспорт": passport_arr,
            "Должность": position_arr,
            "Логин": login_arr,},
            index=None)

    def get_new_id(self):
        max = 0
        for el in self.__employees:
            if el.id > max:
                max = el.id
        return max + 1

    def is_designer(self, id: int):
        if id == 0: return True
        for elem in self.__employees:
            if elem.id == id:
                if elem.position == 1:
                    return True
                else:
                    return False
        return False
    
    def is_manager(self, id: int):
        if id == 0: return True
        for elem in self.__employees:
            if elem.id == id:
                if elem.position == 0:
                    return True
                else:
                    return False
        return False
    
    def is_courier(self, id: int):
        if id == 0: return True
        for elem in self.__employees:
            if elem.id == id:
                if elem.position == 2:
                    return True
                else:
                    return False
        return False

class EmployeesIterator:
    def __init__(self, employees):
        self.__employees = employees
        self._index = 0
    def __len__(self):
        return self.__employees
    def __next__(self):
        try:
            result = self.__employees[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration