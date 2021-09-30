import json
from models.furniture import Furniture
import utils.utils as utils
import os, json
import pandas as pd

class Furnitures:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'repo/furnitures.json')

    def __init__(self):
        self.__furnitures = list()

    def __len__(self):
        return len(self.__furnitures)

    def __iter__(self):
        return FurneturesIterator(self.__furnitures)

    def add(self, furniture: Furniture):
        self.__furnitures.append(furniture)
        return furniture.id
    
    def delete(self, id: int):
        f = self.get_by_id(id)
        if f:
            self.__furnitures.remove(f)
            return True
        return False
    
    def edit(self, id: int, furniture: Furniture):
        f = self.get_by_id(id)
        if f:
            f.kind = furniture.kind
            f.height = furniture.height
            f.width = furniture.width
            f.length = furniture.length
            f.materials = furniture.materials
            f.color = furniture.color
            f.price = furniture.price
            return True
        return False

    def get_by_id(self, id: int):
        for f in self.__furnitures:
            if f.id == id:
                return f
        return None

    def save(self):
        utils.save(self.__filename, self.__furnitures)

    def read(self):
        self.__furnitures = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            furniture = Furniture(elem['id'], elem['kind'], elem['height'], elem['width'], 
                elem['length'], elem['materials'], elem['color'], elem['price'])
            self.add(furniture)

    def get_furnitures_table(self):
        id_arr = []
        kind_arr = []
        height_arr = []
        width_arr = []
        length_arr = []
        materials_arr = []
        color_arr = []
        price_arr = []
        for elem in self.__furnitures:
            id_arr.append(elem.id)
            kind_arr.append(elem.kind)
            height_arr.append(elem.height)
            width_arr.append(elem.width)
            length_arr.append(elem.length)
            materials_arr.append(elem.get_materials_str())
            color_arr.append(elem.color)
            price_arr.append(elem.price)
        return pd.DataFrame(
            {"ИД": id_arr,
            "Вид": kind_arr,
            "Высота": height_arr,
            "Ширина": width_arr,
            "Длина": length_arr,
            "Материалы": materials_arr,
            "Цвет": color_arr,
            "Цена": price_arr,},
            index=None)
    
    def get_new_id(self):
        max = 0
        for el in self.__furnitures:
            if el.id > max:
                max = el.id
        return max + 1

class FurneturesIterator:
    def __init__(self, furnetures):
       self.__furnetures = furnetures
       self._index = 0
    def __next__(self):
        try:
            result = self.__furnetures[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration 