from keebs import db

class Keyboard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    model = db.Column(db.String(64), nullable=False, unique=True)

    def __repr__(self):
        return f"Keyboard({self.brand}, {self.name}, {self.model})"

class Keyset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(64), nullable=False)
    name = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"Keyset({self.brand}, {self.name})"