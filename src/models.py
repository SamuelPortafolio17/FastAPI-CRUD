from sqlalchemy import Column, Integer, String
from .conexion import Base

class Cliente(Base):
    __tablename__="cliente"
    idcliente = Column(Integer,primary_key=True,index=True)
    nombre_cliente = Column(String(45))
    apellido_cliente = Column(String(45))
    cedula = Column(String(8))
    direccion_corta = Column(String(45))
    estado_cuenta = Column(String(8))