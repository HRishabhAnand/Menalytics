from config import db

class Customer(db.Model):
    __tablename__="customer"
    id=db.Column(db.Integer,primary_key=True)
    customer_name=db.Column(db.String(200),nullable=False)
    customer_phone_no=db.Column(db.Integer,nullable=False)
    givenRating = db.relationship('GivenRating', backref='customer')
    orderDetails = db.relationship('OrderDetails', backref='customer')

