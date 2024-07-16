from app import db

class Fabric(db.Model):
    __tablename__ = "fabrics"

    # ForeignKey of the Stock table
    stock_id: int = db.Column(db.Integer, db.ForeignKey("stock.id"), primary_key=True)

    # Own attributes
    width: str = db.Column(db.Float, nullable=False)
    height: str = db.Column(db.Float, nullable=False)

    # Relationship with other tables
    # Stock 1:1
    stock = db.relationship("Stock", back_populates="fabrics", uselist= False)

    