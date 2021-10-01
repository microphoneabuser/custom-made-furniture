from models.employees import Employees
from models.clients import Clients
from models.furnitures import Furnitures
from ref_book import ref_book

class Order:
    def __init__(self, id, client_id, furniture_ids=None, designer_id=None, manager_id=None, 
        courier_id=None, status=0, pre_pay=0.0, cost=0.0):
        self.id = id
        self.client_id = client_id
        self.furniture_ids = furniture_ids
        self.designer_id = designer_id
        self.manager_id = manager_id
        self.courier_id = courier_id
        self.status = status
        self.pre_pay = pre_pay
        self.cost = cost

    def get_furnitures(self, furnitures: Furnitures):
        li = list()
        for i in self.furniture_ids:
            li.append(furnitures.get_by_id(i['id']))
        return li

    def add_furnitures_from_list(self, furs: list):
        if self.furniture_ids == None:
            self.furniture_ids = []
        for fur in furs:
            self.furniture_ids.append({'id': fur})

    def add_furniture(self, fur_id):
        if self.furniture_ids == None:
            self.furniture_ids = []
        self.furniture_ids.append({'id': fur_id})
    
    def del_furniture(self, fur_id):
        self.furniture_ids.remove({'id': fur_id})

    def count_cost(self, all_furnitures: Furnitures):
        cost = 0.0
        for fur_id in self.furniture_ids:
            fur = all_furnitures.get_by_id(fur_id['id'])
            cost += fur.price
        self.cost = cost

    def get_furnitures_str(self, furnitures: Furnitures):
        li = self.get_furnitures(furnitures)
        string = ''
        for f in li:
            string += f'{f.kind} (ИД: {f.id})' + ', '
        return string[:-2] 
    
    def get_client(self, clients: Clients):
        return clients.get_by_id(self.client_id)

    def set_client(self, client_id):
        self.client_id = client_id

    def set_designer(self, designer_id):
        self.designer_id = designer_id

    def set_manager(self, manager_id):
        self.manager_id = manager_id

    def set_courier(self, courier_id):
        self.courier_id = courier_id

    def get_client_str(self, clients: Clients):
        try:
            return self.get_client(clients).fio
        except AttributeError:
            return ''

    def get_designer(self, employees: Employees):
        return employees.get_by_id(self.designer_id)
        

    def get_designer_str(self, employees: Employees):
        try:
            return self.get_designer(employees).fio
        except AttributeError:
            return ''

    def get_manager(self, employees: Employees):
        return employees.get_by_id(self.manager_id)

    def get_manager_str(self, employees: Employees):
        try:
            return self.get_manager(employees).fio
        except AttributeError:
            return ''
    
    def get_courier(self, employees: Employees):
        return employees.get_by_id(self.courier_id)

    def get_courier_str(self, employees: Employees):
        try:
            return self.get_courier(employees).fio
        except AttributeError:
            return ''

    def get_status(self):
        return ref_book.statuses[self.status]

    def get_string(self, *args):
        furnitures = self.get_furnitures_str(args[0])
        client = self.get_client_str(args[1])
        designer = self.get_designer_str(args[2])
        manager = self.get_manager_str(args[2])
        courier = self.get_courier_str(args[2])
        status = self.get_status()
        return f'''
        ИД: {self.id} 
        Мебель: {furnitures}
        Клиент: {client}
        Дизайнер: {designer}
        Менеджер: {manager}
        Курьер: {courier}
        Статус: {status}
        Предоплата: {self.pre_pay}
        Стоимость: {self.cost}
        '''
