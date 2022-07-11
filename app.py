# principal

from flask import Flask
from config import conexion
app=Flask(__name__)

# inicializo mi conexion de mi SQLAlchemy con las base de datos PERO todava no me he conectado.
conexion.init_app(app)

# se ejecuta la conexion y se crearan las tablas, pero si no hay
    # ninguna tabla a crear entonces nos lanzara error de credenciales invalidas.
conexion.create_all(app=app)

if __name__=='__main__':
    app.run(debug=True)
