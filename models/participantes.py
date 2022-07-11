from config import conexion
from sqlalchemy import Column, types
class Participante(conexion.Model):
    # ahora esta clase tendra un comportamiento en forma de una tabla en la bd
        # (todos los atributosque declare que sean propios de la BD se creara como
        #  columnas )
    
    id = Column(type_=types.String(50),autoincrement=True,primary_key=True)
    nombre=Column(type_=types.String(50),nullable=False)
    apellido=Column(type_=types.String(50),nullable=False)
    telefono=Column(type_=types.String(10))
    password=Column(type_=types.Text)
    zona=Column(type_=types.Enum('SUPER_VIP','VIP','GENERAL'),default='GENERAL',nullable=False)
    comentario=Column(type_=types.Text)
    correo=Column(type_=types.String(45),nullable=False)
    # se modificara el nombre de la tabla a nivel de base de datos para que no se llame
        # igual que la clase (en singular y con la primera en mayuscula)
    __tablename__='participantes'