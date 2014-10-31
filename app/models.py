from app import db


class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, default = False)
    preferences = db.relationship('Preference', backref='owner', lazy='dynamic',
                                  uselist=False)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Preference(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    reading = db.Column(db.Integer, nullable= True,default = 0)
    movie = db.Column(db.Integer, nullable= True,default = 0)
    cycling = db.Column(db.Integer, nullable= True,default = 0)
    picnic = db.Column(db.Integer, nullable= True,default = 0)
    climbing = db.Column(db.Integer, nullable= True,default = 0)
    photographing = db.Column(db.Integer, nullable= True,default = 0)
    football = db.Column(db.Integer, nullable= True,default = 0)
    basketball = db.Column(db.Integer, nullable= True,default = 0)
    onlinegame = db.Column(db.Integer, nullable= True,default = 0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Preference %r>' % (self.id)
