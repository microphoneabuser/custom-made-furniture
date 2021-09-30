import itertools

class Person:
    __id_iter = itertools.count()

    def __init__(self, fio, phone, email, passport):
        self.id = next(Person.__id_iter)
        self.fio = fio
        self.phone = phone
        self.email = email
        self.passport = passport
    
    def __init__(self, id, fio, phone, email, passport):
        self.id = id
        self.fio = fio
        self.phone = phone
        self.email = email
        self.passport = passport
    