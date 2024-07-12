from app import db

class Stock(db.Model):
    __tablename__ = "stock"

    # Atributos propios
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount: str = db.Column(db.Integer, nullable=False)