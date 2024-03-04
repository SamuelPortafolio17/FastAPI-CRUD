from pydantic import BaseModel

class Cliente(BaseModel):
    idcliente:int
    nombre_cliente:str 
    apellido_cliente:str 
    cedula:str 
    direccion_corta:str 
    estado_cuenta:str 

    class Config:
        orm_mode=True

class ClienteActualizar(BaseModel):
    nombre_cliente:str 
    apellido_cliente:str 
    cedula:str 
    direccion_corta:str 
    estado_cuenta:str

    class Config:
        orm_mode=True

class Respuesta(BaseModel):
    mensaje:str
