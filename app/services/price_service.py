from typing import List
from app.models import Price
from app.repositories import PriceRepository

repository = PriceRepository()

class PriceService:

    def save(self, price: Price) -> Price:
        #TODO: crear excepción o mensaje 
        if price.price >= 0:
            return repository.save(price)
        else:
            return None
    
    def update(self, price: Price, id: int) -> Price:
        #TODO: crear excepción o mensaje 
        if price.price >= 0:
            return repository.update(price, id)
        else:
            return None
    
    def delete(self, id: int) -> None:
        price = repository.find(id)
        repository.delete(price)
    
    def all(self) -> List[Price]:
        return repository.all()
    
    def find(self, id: int) -> Price:
        return repository.find(id)
    
    def find_by_material_id(self, material_id: int) -> Price:
        return repository.find_by_material_id(material_id)
