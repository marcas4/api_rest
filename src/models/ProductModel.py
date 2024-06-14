from database.db import get_connection
from .entities.Product import Product

class ProductModel():

    @classmethod
    def get_products(self):    
        try:
            connection=get_connection()
            products=[]
        
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, valor_unitario FROM product ORDER BY nombre ASC")
                resultset=cursor.fetchall()

                for row in resultset:
                    product=Product(row[0],row[1],row[2])
                    products.append(product.to_JSON())

            connection.close()
            return products 
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def get_product(self,id):    
        try:
            connection=get_connection()
        
            with connection.cursor() as cursor:
                cursor.execute("SELECT id, nombre, valor_unitario FROM product WHERE id= %s", (id,))
                row =cursor.fetchone()

                product=None
                if row != None:
                    product=Product(row[0],row[1],row[2])
                    product=product.to_JSON()
                
            connection.close()
            return product
        except Exception as ex:
            raise Exception(ex)