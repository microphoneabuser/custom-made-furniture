from models.person import Person

class Client(Person):
    
    def __init__(self, id, fio, phone, email, passport, date_of_birth):
        self.id = id
        self.fio = fio
        self.phone = phone
        self.email = email
        self.passport = passport
        self.date_of_birth = date_of_birth

    def get_string(self):
        return f'''
        ИД: {self.id} 
        ФИО: {self.fio}
        Телефон: {self.phone}
        Email: {self.email}
        Паспорт: {self.passport}
        Дата рождения: {self.date_of_birth}
        '''

    