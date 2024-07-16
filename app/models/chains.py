from app import db

class Chain(db.Model):
    __tablename__ = "chains"

    # ForeignKey of the Material table
    stock_id: int = db.Column(db.Integer, db.ForeignKey("stock.id"), primary_key=True)

    # Own attributes
    meters: str = db.Column(db.Integer, nullable=False)

    # Relationship with other tables
    # Stock 1:1
    stock = db.relationship("Stock", back_populates="chains", uselist= False)

    