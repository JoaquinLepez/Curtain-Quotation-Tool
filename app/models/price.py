from app import db

class Price(db.Model):
    __tablename__ = "prices"

    # Own attributes
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price: str = db.Column(db.Float, nullable=False)

    # ForeignKey of the Material table
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))

    # Relationship with other tables
    # Materials 1:1
    material = db.relationship('Material', back_populates='price', uselist=False)