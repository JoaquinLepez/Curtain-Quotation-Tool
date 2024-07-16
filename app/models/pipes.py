from app import db

class Pipe(db.Model):
    __tablename__ = "pipes"

    # ForeignKey of the Stock table
    stock_id: int = db.Column(db.Integer, db.ForeignKey("stock.id"), primary_key=True)

    # Own attributes
    meters: str = db.Column(db.Float, nullable=False)

    # Relationship with other tables
    # Stock 1:1
    stock = db.relationship("Stock", back_populates="pipes", uselist= False)