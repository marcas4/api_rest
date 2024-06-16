from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    valor_unitario = Column(Integer)

    def __init__(self, id, nombre=None, valor_unitario=None)-> None:
        self.id = id
        self.nombre = nombre
        self.valor_unitario = valor_unitario

    #def __init__(self, id, nombre=None, valor_unitario=None) -> None:
    #    self.id = id
    #    self.nombre = nombre
    #    self.valor_unitario = valor_unitario


    def to_JSON(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'valor_unitario': self.valor_unitario
        }