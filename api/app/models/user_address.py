from api.app.database.instance import db

class UserAddress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(100))
    number = db.Column(db.Integer())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="address")

    def __repr__(self):
        return '<UserAddress %r>' % self.street