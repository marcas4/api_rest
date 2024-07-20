
# api_rest

Api REST que se conecta a una base de datos PostgreSQL con las funcionalidades para realizar un CRUD


## Tabla de contenido

#### Marco Teórico
#### Funcionamiento
#### API Reference
#### Modelo de datos
#### Tecnologías
#### Elaborado por


### Marco Teórico
Gracias al avance de la tecnología, las personas pueden ayudarse con herramientas tecnológicas para realizar su trabajo de manera mas eficiente, aún mas si se trata de personas con discapacidad.
La tecnología ha demostrado ser una aliada fundamental para mejorar la calidad de vida de las personas con discapacidad, ayudando a la inclusión social, al permitirles participar activamente en el ámbito laboral, dando empoderamiento y brindando herramientas que les permiten desarrollar sus habilidades.
Su constante evolución y desarrollo continuo abren las puertas a un futuro cada vez mas accesible e igualitario para todos.
Las aplicaciones web pueden ser una gran ayuda para personas con discapacidad que les faciliten sus tareas tanto diarias como laborales.
La tecnología ha abierto un mundo de oportunidades brindándoles herramientas que les permiten participar activamente en la sociedad, les otorga autonomía, acceso a la información, acceso a la comunicación así como oportunidades laborales.
En este contexto, se ha creado esta API REST que hace parte del programa Pedidos en Restaurante, que permitirá que personas con discapacidad cognitiva puedan trabajar en un restaurante tomando el pedido de los clientes, eligiendo de una lista predeterminada con precios y posteriormente llevando la orden a su mesa.




## Funcionamiento

Este software puede ser probado desde un cliente como postman desde donde se puede consumir su servicio GET, POST, PUT y DELETE  
Se debe conectar a una base de datos Postgres con la siguiente entidad:

```http
  CREATE TABLE IF NOT EXISTS product (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255),
            valor_unitario INTEGER
        )
```

Como ejemplo de producto se puede utilizar el siguiente insert:

```http
 INSERT INTO product (nombre, valor_unitario)
      VALUES ('Arepa con queso', 3500)
```





## API Reference

#### Get all items

```http
  GET /api/productos
```

#### Get item

```http
  GET /api/productos/${id}
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :--------------------------------   |
| `id`      | `string` | **Required**. Id del artículo a mostrar |

#### Post item

```http
  POST /api/productos/add
```
| Parameter | Type     | Description                         |
| :-------- | :------- | :--------------------------------   |
| `nombre`  | `string` | **Required**. nombre del artículo |
| `valor_unitario`  | `string` | **Required**. valor del artículo|

#### Put item

```http
  PUT /api/productos/update/${id}
```
| Parameter | Type     | Description                         |
| :-------- | :------- | :--------------------------------   |
| `nombre`  | `string` | **Required**. nombre del artículo   |
| `valor_unitario`| `string` | **Required**. valor del articulo |

#### Delete item

```http
  DELETE /api/productos/${id}
```

| Parameter | Type     | Description                         |
| :-------- | :------- | :--------------------------------   |
| `id`     | `string` | **Required**. Id del artículo a borrar  |

### Modelo de datos
![Modelo de datos](modeloDeDatos.png?raw=true)

### Tecnologías

- Python 3
- Framework flask



## Elaborado por:

Nombre: Marcia Castro Moya

Email: marcas4@gmail.com

X: @marcas4


