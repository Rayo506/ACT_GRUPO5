from fastapi import APIRouter, HTTPException
from app.models.items import ProductCreate, ProductUpdate
from app.crud import product_store

router = APIRouter(prefix="/figuras", tags=["figuras"])

@router.post("/")
def create_product(product: ProductCreate):
    new_product = product_store.create_product(product)
    return new_product

@router.get("/")
def get_all_products():
    return product_store.get_all_products()

@router.get("/{product_id}")
def get_product(product_id: int):
    product = product_store.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Figura no encontrada")
    return product

@router.put("/{product_id}")
def update_product(product_id: int, product_update: ProductUpdate):
    updated = product_store.update_product(product_id, product_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Figura no encontrada")
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: int):
    success = product_store.delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Figura no encontrada")
    return {"message": "Figura eliminada"}

@router.get("/search")
def search(category: str | None = None):
    results = product_store.search_products(category)
    return results
s