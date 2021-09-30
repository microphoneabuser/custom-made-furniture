import json
import hashlib
from os import close 

def gen_hash(string):
    m = string.encode('utf-8')
    m = hashlib.sha256(m)
    return m.hexdigest()

def save(path, collection): 
    class ComplexEncoder(json.JSONEncoder):
        def default(self, z):
            if isinstance(z, complex):
                return (z.real, z.imag)
            return super().default(z)

    with open(path, 'w', encoding='utf-8') as write:
        json.dump(collection, write, default=lambda o: o.__dict__, 
            cls=ComplexEncoder)
    
