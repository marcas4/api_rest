from flask import Flask

from config import config

#Routes
from routes import Producto

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprint
    app.register_blueprint(Producto.main, url_prefix='/api/productos')

    #Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()
