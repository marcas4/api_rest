from models.entities import Product
from database.db import engine
from sqlalchemy.orm import sessionmaker

from database.db import get_connection
from .entities.Product import Product

Session = sessionmaker(bind=engine)

class ProductModel():

    @classmethod
    def get_products(self):
        try:
            session = Session()
            products = session.query(Product).order_by(Product.nombre).all()
            session.close()
            return [product.to_JSON() for product in products]
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_product(self,id):    
        try:
            session = Session()
        
            product = session.query(Product).filter_by(id=id).first()
            session.close()
            
            if product:
               return product.to_JSON()
            else:    
               return None
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def add_product(self, product):    
        try:
            session = Session()
            session.add(product)  # Agrega el objeto Product a la sesión
            session.commit() # Guarda los cambios en la base de datos
                          
            session.close()
            return 1  # Retorna la cantidad de filas afectadas (1 en este caso)
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_product(self, product):    
        try:
            session = Session()
            product_to_delete = session.query(Product).get(product.id)
            session.delete(product_to_delete)
            session.commit()    
            return 1  # Retorna la cantidad de filas afectadas (1 en este caso)
            
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_product(self, id, nombre, valor_unitario):    
        try:
            session = Session()
            product_to_update = session.query(Product).get(id)
            if product_to_update:
                product_to_update.nombre = nombre
                product_to_update.valor_unitario = valor_unitario
                session.commit()
                return 1
            else:
                return 0
        except Exception as ex:
            raise Exception(ex) 