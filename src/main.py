from fastapi import Depends, FastAPI
from . import models,esquemas
from .conexion import SessionLocal,engine
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get("/clientes/", response_model=List[esquemas.Cliente])
def mostrar_clientes(db:Session=Depends(get_db)):
    clientes = db.query(models.Cliente).all()
    return clientes

@app.put("/clientes/{idcliente}", response_model=esquemas.Cliente)
def actualizar_cliente(idcliente:int, entrada:esquemas.ClienteActualizar, db:Session=Depends(get_db)):
    cliente = db.query(models.Cliente).filter_by(idcliente=idcliente).first()
    cliente.nombre_cliente=entrada.nombre_cliente
    cliente.apellido_cliente=entrada.apellido_cliente
    cliente.cedula=entrada.cedula
    cliente.direccion_corta=entrada.direccion_corta
    cliente.estado_cuenta=entrada.estado_cuenta
    db.commit()
    db.refresh(cliente)
    return cliente

@app.post("/clientes/", response_model=esquemas.Cliente)
def crear_cliente(entrada:esquemas.Cliente, db:Session=Depends(get_db)):
    cliente = models.Cliente(nombre_cliente=entrada.nombre_cliente, apellido_cliente=entrada.apellido_cliente, cedula=entrada.cedula, direccion_corta=entrada.direccion_corta, estado_cuenta=entrada.estado_cuenta)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente

@app.delete("/clientes/{idcliente}", response_model=esquemas.Respuesta)
def borrar_cliente(idcliente:int, db:Session=Depends(get_db)):
    cliente = db.query(models.Cliente).filter_by(idcliente=idcliente).first()
    db.delete(cliente)
    db.commit()
    respuesta = esquemas.Respuesta(mensaje="CLIENTE ELIMINADO EXITOSAMENTE")
    return respuesta