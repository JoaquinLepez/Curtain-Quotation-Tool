from app import db

class Stock(db.Model):
    __tablename__ = "stock"

    # Own attributes
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount: str = db.Column(db.Integer, nullable=False)

    # ForeignKey of the Material table
    material_id: int = db.Column(db.Integer, db.ForeignKey("materials.id"))

    # Relationship with other tables
    # Materials 1:N
    material = db.relationship("Material", back_populates="stock")

    # Chains 1:1
    chains = db.relationship("Chain", back_populates="stock", uselist=False)

    # Mechanisms 1:1
    mechanisms = db.relationship("Mechanism", back_populates="stock", uselist=False)

    # Pipes 1:1
    pipes = db.relationship("Pipe", back_populates="stock", uselist=False)


    