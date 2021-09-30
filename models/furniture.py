class Furniture:

    def __init__(self, id, kind, height, width, length, materials, color, price):
        self.id = id
        self.kind = kind
        self.height = height
        self.width = width
        self.length = length
        self.materials = materials
        self.color = color
        self.price = price

    def add_material(self, material: str):
        m = {'name': material}
        self.materials.append(m)
    
    def del_material(self, material: str):
        m = {'name': material}
        self.materials.remove(m)

    def get_materials_str(self):
        string = ''
        for m in self.materials:
            string += m['name'] + ', '
        return string[:-2]

    def get_string(self):
        materials = self.get_materials_str()
        return f'''
        ИД: {self.id} 
        Вид: {self.kind}
        Высота: {self.height}
        Ширина: {self.width}
        Длина: {self.length}
        Материалы: {materials}
        Цвет: {self.color}
        Цена: {self.price}
        '''
