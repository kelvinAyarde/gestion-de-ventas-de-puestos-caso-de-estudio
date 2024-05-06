from flask import Flask
from flask_mysqldb import MySQL
from config import ConfigDesarrollo
#rutas
from routes import Inicio_route,Venta_route,Pago_route

app = Flask(__name__)

if __name__ == '__main__':
    app.config.from_object(ConfigDesarrollo)
    mysql = MySQL(app)
    #blueprints
    app.register_blueprint(Inicio_route.inicio, url_prefix='/')
    app.register_blueprint(Venta_route.venta, url_prefix='/venta')
    app.register_blueprint(Pago_route.pago, url_prefix='/pago')
    #---------------
    app.run()
