from api.app.database.instance import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.relationship("UserAddress", back_populates="user", cascade="all, delete-orphan")
    phone = db.Column(db.String(15), unique=True)

    def __repr__(self):
        return "<User(username='%s', email='%s', address='%s')>" % (self.username, self.email, self.address)