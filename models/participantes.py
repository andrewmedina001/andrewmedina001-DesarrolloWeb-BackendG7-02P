from config import conexion
from sqlalchemy import Column
class Participante(conexion.Model):
    # ahora esta clase tendra un comportamiento en forma de una tabla en la bd
        # (todos los atributosque declare que sean propios de la BD se creara como
        #  columnas )
    id = conexion.Column()
