from typing import List
from app.models import Price
from app import db

class PriceRepository:

    def save(self, price: Price) -> Price:
        db.session.add(price) 
        db.session.commit()
        return Price
    
    def update(self, price: Price, id: int) -> Price:
        entity = self.find(id)
        if entity is None:
            return None
        
        entity.price = price.price
 
        db.session.add(entity)
        db.session.commit()
        return entity
    
    def delete(self, price: Price) -> None:
        db.session.delete(price)
        db.session.commit()
    
    def all(self) -> List[Price]:
        prices = db.session.query(Price).all()
        return prices
    
    def find(self, id: int) -> Price:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Price).filter(Price.id == id).one()
        except:
            return None
        
    def find_by_material_id(self, material_id: int) -> Price:
        return db.session.query(Price).filter(Price.material_id == material_id).one_or_none()
    
