from typing import List, Optional, Dict
from app.models.items import Product, ProductCreate, ProductUpdate

class ProductStore:
    def __init__(self):
        self.products: Dict[int, Product] = {}
        self.next_id: int = 1

    def create_product(self, product: ProductCreate) -> Product:
        product_dict = product.dict()
        product_dict["id"] = self.next_id
        new_product = Product(**product_dict)
        self.products[self.next_id] = new_product
        self.next_id += 1
        return new_product

    def get_product(self, product_id: int) -> Optional[Product]:
        return self.products.get(product_id)

    def get_all_products(self) -> List[Product]:
        return list(self.products.values())

    def update_product(self, product_id: int, product_update: ProductUpdate) -> Optional[Product]:
        if product_id not in self.products:
            return None
        existing = self.products[product_id]
        update_data = product_update.dict(exclude_unset=True)
        updated = existing.copy(update=update_data)
        self.products[product_id] = updated
        return updated

    def delete_product(self, product_id: int) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False

    def search_products(self, category: Optional[str] = None) -> List[Product]:
        results = list(self.products.values())
        if category:
            results = [p for p in results if p.categoria.lower() == category.lower()]
        return results


product_store = ProductStore()
