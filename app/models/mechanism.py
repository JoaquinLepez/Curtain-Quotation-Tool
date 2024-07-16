from app import db

class Mechanism(db.Model):
    __tablename__ = "mechanisms"

    # ForeignKey of the Stock table
    stock_id: int = db.Column(db.Integer, db.ForeignKey("stock.id"), primary_key=True)

    # Own attributes
    units: str = db.Column(db.Integer, nullable=False)

    # Relationship with other tables
    # Stock 1:1
    stock = db.relationship("Stock", back_populates="mechanisms", uselist= False)

    