import json
from models.client import Client
import os, json
import utils.utils as utils
import pandas as pd

class Clients:
    __dir = os.path.dirname(__file__)
    __filename = os.path.join(__dir,'../', 'repo/clients.json')

    def __init__(self):
        self.__clients = list()

    def __len__(self):
        return len(self.__clients)

    def __iter__(self):
        return ClientsIterator(self.__clients)

    def add(self, client: Client):
        self.__clients.append(client)
        return client.id
    
    def delete(self, id: int):
        cl = self.get_by_id(id)
        if cl:
            self.__clients.remove(cl)
            return True
        return False
    
    def edit(self, id: int, client: Client):
        cl = self.get_by_id(id)
        if cl:
            cl.fio = client.fio
            cl.phone = client.phone
            cl.email = client.email
            cl.passport = client.passport
            cl.date_of_birth = client.date_of_birth
            return True
        return False

    def get_by_id(self, id: int):
        for cl in self.__clients:
            if cl.id == id:
                return cl
        return None

    def save(self): 
        utils.save(self.__filename, self.__clients)

    def read(self):
        self.__clients = list()
        file = open(self.__filename, 'r', encoding='utf-8')
        data = json.loads(file.read())
        for elem in data:
            client = Client(elem['id'], elem['fio'], elem['phone'], elem['email'], 
                elem['passport'], elem['date_of_birth'])
            self.add(client)

    def get_clients_table(self):
        id_arr = []
        fio_arr = []
        phone_arr = []
        email_arr = []
        passport_arr = []
        date_of_birth_arr = []
        for elem in self.__clients:
            id_arr.append(elem.id)
            fio_arr.append(elem.fio)
            phone_arr.append(elem.phone)
            email_arr.append(elem.email)
            passport_arr.append(elem.passport)
            date_of_birth_arr.append(elem.date_of_birth)
        return pd.DataFrame(
            {"ИД": id_arr,
            "ФИО": fio_arr,
            "Номер телефона": phone_arr,
            "Email": email_arr,
            "Паспорт": passport_arr,
            "Дата рождения": date_of_birth_arr,},
            index=None)

    def get_new_id(self):
        max = 0
        for el in self.__clients:
            if el.id > max:
                max = el.id
        return max + 1

class ClientsIterator:
    def __init__(self, clients):
        self.__clients = clients
        self._index = 0
    def __next__(self):
        try:
            result = self.__clients[self._index]
            self._index +=1
            return result
        except IndexError:
           self._index = 0
           raise StopIteration    