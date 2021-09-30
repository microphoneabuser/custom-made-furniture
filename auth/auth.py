from models.employees import Employees
from utils import utils

def authorize(login, password):
    users = Employees()
    users.read()
    for user in users:
        if user.login == login:
            if user.password_hash == utils.gen_hash(password):
                return user, 'Вы успешно вошли в учетную запись!'
            else:
                return None, 'Вы ввели неправильный пароль!'
    
    return None, 'Вы ввели неправильный логин и пароль!'
