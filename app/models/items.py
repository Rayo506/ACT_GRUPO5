from pydantic import BaseModel

class Product(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int
    categoria: str

class ProductCreate(BaseModel):
    nombre: str
    precio: float
    stock: int
    categoria: str

class ProductUpdate(BaseModel):
    nombre: str | None = None
    precio: float | None = None
    stock: int | None = None
    categoria: str | None = None
