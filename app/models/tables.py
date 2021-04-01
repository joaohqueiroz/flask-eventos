from app import db


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    where = db.Column(db.String)
    date = db.Column(db.DateTime)
    registered = db.Column(db.Boolean)
    image = db.Column(db.String)

    def __init__(self, title, description, where, date, image):
        self.title = title
        self.description = description
        self.where = where
        self.date = date
        self.registered = False
        self.image = image

    def __repr__(self):
        return "<Post %r>" % self.id
