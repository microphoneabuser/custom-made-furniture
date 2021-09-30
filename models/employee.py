from models.person import Person
import utils.utils as utils
from ref_book import ref_book

class Employee(Person):

    def __init__(self, id, fio, phone, email, passport, position, login, password_hash):
        self.id = id
        self.fio = fio
        self.phone = phone
        self.email = email
        self.passport = passport
        self.position = position
        self.login = login
        self.password_hash = password_hash

    def set_password(self, password):
        self.password_hash = utils.gen_hash(password)

    def get_position(self):
        return ref_book.positions[self.position]

    def get_string(self):
        position = self.get_position()
        return f'''
        ИД: {self.id} 
        ФИО: {self.fio}
        Телефон: {self.phone}
        Email: {self.email}
        Паспорт: {self.passport}
        Должность: {position}
        Логин: {self.login}
        Хеш пароля: {self.password_hash}
        '''
