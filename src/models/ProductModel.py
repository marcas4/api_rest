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
        
    @classmethod
    def add_product(self, product):    
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO product (nombre, valor_unitario) 
                                VALUES(%s, %s)""", (product.nombre,product.valor_unitario))
                affected_rows=cursor.rowcount
                connection.commit()
                          
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def delete_product(self, product):    
        try:
            connection=get_connection()
        
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM product WHERE id = %s", (product.id,))
                affected_rows=cursor.rowcount
                connection.commit()    
                
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    @classmethod
    def update_product(self, product):    
        try:
            connection=get_connection()
            with connection.cursor() as cursor:
                cursor.execute("""UPDATE product SET nombre = %s, valor_unitario = %s 
                                WHERE id = %s""", (product.nombre,product.valor_unitario,product.id))
                affected_rows=cursor.rowcount
                connection.commit()
                          
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)