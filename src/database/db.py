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
engine = create_engine('postgresql://produc_user:kaFVAfj2cDrXJHfkycDSw2gCF92O5iLX@dpg-cq81ei0gph6c73bko53g-a.oregon-postgres.render.com/produc')