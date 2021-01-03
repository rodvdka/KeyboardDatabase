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

def resetTempData():
    print("Resetting Temp Data")
    db.drop_all()
    db.session.add(Keyboard(brand="IBM", name="Model M SSK Industrial Mopar", model="1395682"))
    db.session.add(Keyboard(brand="NEC", name="PC-8801 MKII SR", model="8801"))
    db.session.add(Keyboard(brand="IBM", name="5251 Beamspring", model="5251"))
    db.session.add(Keyset(brand="GMK", name="Hyperfuse"))
    db.session.commit()