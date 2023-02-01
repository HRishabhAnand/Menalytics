from config import db


class OrderDetails(db.Model):
    __tablename__ = 'orderDetails'      
    id = db.Column(db.Integer, primary_key=True)
    customer_name=db.Column(db.String(200),nullable=False)
    quantity_of_items = db.Column(db.Integer, primary_key=False)
    total_amount = db.Column(db.Integer, primary_key=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))



