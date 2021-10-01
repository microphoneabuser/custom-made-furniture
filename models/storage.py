import json
from models.furniture import Furniture
from models.furnitures import Furnitures
import utils.utils as utils
import os, json
import pandas as pd

class Storage:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'repo/storage.json')

    def __init__(self):
        self.__storage = {}

    def __len__(self):
        return len(self.__storage)

    def __iter__(self):
        return StorageIterator(self.__storage)

    def add(self, fur_id: int, quantity: int):
        self.__storage[fur_id] = quantity
        return fur_id
    
    def delete(self, id: int):
        if self.get_by_id(id):
            del self.__storage[id]
            return True
        return False
    
    def edit_add(self, id: int, quantity: int):
        if self.get_by_id(id):
            self.__storage[id] += quantity
            return True
        return False

    def edit_del(self, id: int, quantity: int):
        if self.get_by_id(id):
            if self.__storage[id] - quantity < 0:
                return False
            self.__storage[id] -= quantity
            if self.__storage[id] == 0:
                self.delete(id)
            return True
        return False

    def get_by_id(self, id: int):
        for f in self.__storage.keys():
            if f == id:
                return True
        return False

    def get_by_id_str(self, id: int, furs: Furnitures):
        try:
            fur = furs.get_by_id(id)
            materials = fur.get_materials_str()
            return f'''
            ИД: {fur.id} 
            Вид: {fur.kind}
            Высота: {fur.height}
            Ширина: {fur.width}
            Длина: {fur.length}
            Материалы: {materials}
            Цвет: {fur.color}
            Цена: {fur.price}
            Количество: {self.__storage[id]}
            '''
        except:
            return None

    def save(self):
        utils.save(self.__filename, self.__storage)

    def read(self):
        self.__storage = dict()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            self.add(int(elem), data[elem])

    def get_storage_table(self, furnitures: Furnitures):
        id_arr = []
        kind_arr = []
        height_arr = []
        width_arr = []
        length_arr = []
        materials_arr = []
        color_arr = []
        price_arr = []
        quantity_arr = []
        for i in self.__storage:
            elem = furnitures.get_by_id(i)
            id_arr.append(elem.id)
            kind_arr.append(elem.kind)
            height_arr.append(elem.height)
            width_arr.append(elem.width)
            length_arr.append(elem.length)
            materials_arr.append(elem.get_materials_str())
            color_arr.append(elem.color)
            price_arr.append(elem.price)
            quantity_arr.append(self.__storage[i])
        return pd.DataFrame(
            {"ИД": id_arr,
            "Вид": kind_arr,
            "Высота": height_arr,
            "Ширина": width_arr,
            "Длина": length_arr,
            "Материалы": materials_arr,
            "Цвет": color_arr,
            "Цена": price_arr,
            "Количество": quantity_arr,},
            index=None)
    
    def get_new_id(self):
        max = 0
        for el in self.__furnitures:
            if el.id > max:
                max = el.id
        return max + 1

class StorageIterator:
    def __init__(self, storage):
       self.__storage = storage
       self._index = 0
    def __next__(self):
        try:
            result = self.__storage[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration 