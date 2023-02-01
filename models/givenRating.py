from config import db


class GivenRating(db.Model):
    __tablename__ = 'givenRating'      
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, primary_key=False)
    customer_name=db.Column(db.String(200),nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))




