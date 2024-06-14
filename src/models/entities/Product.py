class Product():

    def __init__(self, id, nombre=None, valor_unitario=None) -> None:
        self.id = id
        self.nombre = nombre
        self.valor_unitario = valor_unitario


    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'valor_unitario': self.valor_unitario
        }