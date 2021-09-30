import json
from models.order import Order
import utils.utils as utils
import os, json
import pandas as pd

class Orders:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'repo/orders.json')

    def __init__(self):
        self.__orders = list()

    def __len__(self):
        return len(self.__orders)

    def __iter__(self):
        return OrdersIterator(self.__orders)

    def add(self, order: Order):
        self.__orders.append(order)
        return order.id
    
    def delete(self, id: int):
        ord = self.get_by_id(id)
        if ord:
            self.__orders.remove(ord)
            return True
        return False
    
    def edit(self, id: int, order: Order):
        ord = self.get_by_id(id)
        if ord:
            ord.furniture_ids = order.furniture_ids
            ord.client_id = order.client_id
            ord.designer_id = order.designer_id
            ord.manager_id = order.manager_id
            ord.courier_id = order.courier_id
            ord.status = order.status
            ord.pre_pay = order.pre_pay
            ord.cost = order.cost
            return True
        return False

    def get_by_id(self, id: int):
        for ord in self.__orders:
            if ord.id == id:
                return ord
        return None
    
    def save(self):
        utils.save(self.__filename, self.__orders)

    def read(self):
        self.__orders = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            order = Order(elem['id'], elem['client_id'], elem['furniture_ids'], elem['designer_id'], 
                elem['manager_id'], elem['courier_id'], elem['status'], elem['pre_pay'], elem['cost'])
            self.add(order)

    def get_orders_table(self, furnitures, clients, employees):
        id_arr = []
        furnitures_arr = []
        client_arr = []
        designer_arr = []
        manager_arr = []
        courier_arr = []
        status_arr = []
        pre_pay_arr = []
        cost_arr = []
        for elem in self.__orders:
            id_arr.append(elem.id)
            furnitures_arr.append(elem.get_furnitures_str(furnitures))
            client_arr.append(elem.get_client_str(clients))
            designer_arr.append(elem.get_designer_str(employees))
            manager_arr.append(elem.get_manager_str(employees))
            courier_arr.append(elem.get_courier_str(employees))
            status_arr.append(elem.get_status())
            pre_pay_arr.append(elem.pre_pay)
            cost_arr.append(elem.cost)
        return pd.DataFrame(
            {"ИД": id_arr,
            "Мебель": furnitures_arr,
            "Клиент": client_arr,
            "Дизайнер": designer_arr,
            "Менеджер": manager_arr,
            "Курьер": courier_arr,
            "Статус": status_arr,
            "Предоплата": pre_pay_arr,
            "Стоимость": cost_arr,},
            index=None)

    def get_new_id(self):
        max = 0
        for el in self.__orders:
            if el.id > max:
                max = el.id
        return max + 1


class OrdersIterator:
   def __init__(self, orders):
       self.__orders = orders
       self._index = 0
   def __next__(self):
        try:
            result = self.__orders[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration