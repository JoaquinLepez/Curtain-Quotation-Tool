from app import db

class Material(db.Model):
    __tablename__ = "materials"

    # Own attributes
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(80), nullable=False)
    description: str = db.Column(db.String(80), nullable=False)
    measuring_unit: str = db.Column(db.String(80), nullable=False)

    # Relationship with other tables
    # prices 1:1
    price = db.relationship("Price", back_populates="material", uselist=False)

    # # Stock N:M
    # stock = db.relationship("Stock", back_populates="material")

    