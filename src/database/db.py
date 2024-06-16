import psycopg2 
from psycopg2 import DatabaseError
from decouple import config
from sqlalchemy import create_engine


def get_connection():
    try:
        return psycopg2.connect(
            host=config('PGSQL_HOST'),
            user=config('PGSQL_USER'),
            password=config('PGSQL_PASSWORD'),
            port=config('PGSQL_PORT'),            
            database=config('PGSQL_DATABASE')
            
        )
    except DatabaseError as ex:
        raise ex 
    
    # Configura la conexión a la base de datos
engine = create_engine('postgresql://gescas:oOu5gVJ746zOjOgaKmiAJDtOy2b955b2@dpg-cpjnge821fec73a109u0-a.oregon-postgres.render.com:5432/products_kt0r')